import socket
import sys
import settings
import json
import logging


TIMEOUT = 0.1
BLOCK = 1024


logger = logging.getLogger('http_responses')


class Client:

    @staticmethod
    def create_socket():

        try:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.settimeout(1)
            return new_socket
        except socket.error as e:
            print('Failed to create socket.' + 'Error code: ' + str(e[0]) + ' , Error message : ' + e[1])
            sys.exit()

    @staticmethod
    def create_client():

        host = settings.MOCK_HOST
        port = int(settings.MOCK_PORT)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(TIMEOUT)
        client.connect((host, port))

        return client

    @staticmethod
    def receive_data(client):

        total_data = []

        data = client.recv(BLOCK)
        if data:
            total_data.append(data.decode())
        else:
            client.close()

        while True:
            data = client.recv(BLOCK)
            if data:
                total_data.append(data.decode())
            else:
                client.close()
                break

        data = ''.join(total_data).splitlines()

        data[-1] = json.loads(data[-1])

        logger.info('RESPONSE:   ' + str(data))

        return data

    def get_request(self, name):

        client = self.create_client()

        host = settings.MOCK_HOST
        params = '/get_user/' + str(name)

        request = f'GET {params} HTTP/1.1\r\n' \
                  f'Host:{host}\r\n\r\n'

        client.send(request.encode())
        logger.info('REQUEST:   ' + str(request).replace('\r\n', ', '))

        data = self.receive_data(client)

        return data

    def post_request(self, human_data):

        client = self.create_client()

        host = settings.MOCK_HOST
        port = settings.MOCK_PORT

        data = human_data
        data = json.dumps(data)
        length = len(data)

        request = f'POST /add_user HTTP/1.1\r\n' \
                  f'Host:{host}:{port}\r\n' \
                  f'Content-Length:{length}\r\n' \
                  f'Content-type:application/json\r\n\r\n' \
                  f'{data}'

        client.send((request.encode()))
        logger.info('REQUEST:   ' + str(request).replace('\r\n', ', '))

        data = self.receive_data(client)

        return data

    def put_request(self, human_data):

        client = self.create_client()

        params = '/change_user_data/' + str(human_data['name'])
        host = settings.MOCK_HOST

        data = {'id': human_data['id'], 'surname': human_data['surname'], 'age': human_data['age']}
        data = json.dumps(data)
        length = len(data)

        request = f'PUT {params} HTTP/1.1\r\n' \
                  f'Host:{host}\r\n' \
                  f'Content-Length:{length}\r\n' \
                  f'Content-type:application/json\r\n\r\n' \
                  f'{data}'

        client.send((request.encode()))
        logger.info('REQUEST:   ' + str(request).replace('\r\n', ', '))

        data = self.receive_data(client)

        return data

    def delete_request(self, name):

        client = self.create_client()

        params = '/change_user_data/' + str(name)
        host = settings.MOCK_HOST

        request = f'DELETE {params} HTTP/1.1\r\n' \
                  f'Host:{host}\r\n' \
                  f'Content-type:application/json\r\n\r\n'

        client.send((request.encode()))
        logger.info('REQUEST:   ' + str(request).replace('\r\n', ', '))

        data = self.receive_data(client)

        return data
