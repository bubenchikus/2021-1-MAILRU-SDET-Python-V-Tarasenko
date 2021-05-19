import socket
import sys
import settings
import json
import logging


TIMEOUT = 0.1
BLOCK = 1024


logger = logging.getLogger('http_responses')


class Client():

    @staticmethod
    def create_socket():

        try:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

        while True:
            data = client.recv(BLOCK)
            if data:
                total_data.append(data.decode())
            else:
                client.close()
                break

        data = ''.join(total_data).splitlines()

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

    def post_request(self, name):

        client = self.create_client()

        host = settings.MOCK_HOST
        port = settings.MOCK_PORT

        data = {'name': name}
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

    def put_request(self, name, new_surname, new_age):

        client = self.create_client()

        params = '/change_user_data/' + str(name)
        host = settings.MOCK_HOST

        data = {'surname': new_surname, 'age': new_age}
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

        params = '/delete_user_data/' + str(name)
        host = settings.MOCK_HOST

        request = f'DELETE {params} HTTP/1.1\r\n' \
                  f'Host:{host}'

        client.send((request.encode()))
        logger.info('REQUEST:   ' + str(request).replace('\r\n', ', '))
