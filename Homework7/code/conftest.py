import os
import signal
import subprocess
import time
from copy import copy
import requests
from requests.exceptions import ConnectionError
import settings
import pytest
import logging

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def start_app(config):
    app_path = os.path.join(repo_root, 'app', 'app.py')

    app_out = open('/tmp/app_stdout.log', 'w')
    app_err = open('/tmp/app_stderr.log', 'w')

    env = copy(os.environ)
    env['APP_HOST'] = settings.APP_HOST
    env['APP_PORT'] = settings.APP_PORT

    env['STUB_HOST'] = settings.STUB_HOST
    env['STUB_PORT'] = settings.STUB_PORT

    env['MOCK_HOST'] = settings.MOCK_HOST
    env['MOCK_PORT'] = settings.MOCK_PORT

    proc = subprocess.Popen(['python3.8', app_path], stdout=app_out, stderr=app_err, env=env)

    config.app_proc = proc
    config.app_out = app_out
    config.app_err = app_err

    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{settings.APP_HOST}:{settings.APP_PORT}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def start_mock():
    from mock import flask_mock
    flask_mock.run_mock()

    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('Mock did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()
        start_app(config)


def stop_app(config):
    config.app_proc.send_signal(signal.SIGINT)
    exit_code = config.app_proc.wait()

    config.app_out.close()
    config.app_err.close()

    assert exit_code == 0


def stop_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_app(config)
        stop_mock()


@pytest.fixture(scope='session', autouse=True)
def logger():

    log_file = os.path.join('/tmp/http_response_logger.log')

    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setLevel(log_level)

    log = logging.getLogger('http_responses')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()
