import threading
import settings
import json

from flask import Flask, jsonify, request

from app.app import app_data

app = Flask(__name__)

SURNAME_DATA = {}
CHANGE_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):

    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not found'), 404


@app.route('/change_data/<name>', methods=['PUT'])
def change_data(name):

    if new_data := CHANGE_DATA.get(name):
        return jsonify({'surname': new_data[0], 'age': new_data[1]}), 200
    else:
        return jsonify(f'New data for user {name} not found'), 404


@app.route('/change_data_2/<name>', methods=['PUT'])
def change_data_2(name):

    new_surname = json.loads(request.data)['surname']
    new_age = json.loads(request.data)['age']

    app_data[name]['surname'] = 'redhtsrhjtsryujsty'

    if name in app_data:
        app_data[name]['surname'] = new_surname
        app_data[name]['age'] = new_age
        data = {'surname': new_surname, 'age': new_age}
        return jsonify(data), 201
    else:
        return jsonify(f'New data for user {name} not found'), 404


@app.route('/delete_data/<name>', methods=['DELETE'])
def delete_data(name):

    if name in app_data:
        del app_data['name']
        return jsonify(f'Data for {name} was successfully deleted'), 204
    else:
        return jsonify(f'New data for user {name} not found'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
