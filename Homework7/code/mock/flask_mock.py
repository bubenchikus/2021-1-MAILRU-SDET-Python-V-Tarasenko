import threading
import settings
import json


from flask import Flask, jsonify, request


app = Flask(__name__)
USER_DATA = {}
user_id_seq = 1


@app.route('/add_user', methods=['POST'])
def create_user():
    global user_id_seq

    user_name = json.loads(request.data)['name']

    surname = json.loads(request.data)['surname']
    age = json.loads(request.data)['age']

    if user_name not in USER_DATA:
        USER_DATA[user_name] = {}
        USER_DATA[user_name]['id'] = user_id_seq
        USER_DATA[user_name]['surname'] = surname
        USER_DATA[user_name]['age'] = age

        data = {'user_id': user_id_seq, 'surname': surname, 'age': age}
        user_id_seq += 1
        return jsonify(data), 201
    else:
        return jsonify(f'User name {user_name} already exists: if {USER_DATA[user_name]}'), 400


@app.route('/get_user/<name>', methods=['GET'])
def get_user_data(name):

    if USER_DATA.get(name):

        data = {'user_id': USER_DATA[name]['id'],
                'surname': USER_DATA[name]['surname'],
                'age': USER_DATA[name]['age']
                }

        return jsonify(data), 200
    else:
        return jsonify(f'User name {name} not found'), 404


@app.route('/change_user_data/<name>', methods=['PUT', 'DELETE'])
def change_user_data(name):

    if USER_DATA.get(name):
        if request.method == 'PUT':
            USER_DATA[name]['id'] = json.loads(request.data)['id']
            USER_DATA[name]['surname'] = json.loads(request.data)['surname']
            USER_DATA[name]['age'] = json.loads(request.data)['age']

            data = {'user_id': USER_DATA[name]['id'],
                    'surname': USER_DATA[name]['surname'],
                    'age': USER_DATA[name]['age']
                    }
        else:
            del USER_DATA[name]
            data = None
        return jsonify(data), 200
    else:
        return jsonify(f'User name {name} not found'), 404


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
