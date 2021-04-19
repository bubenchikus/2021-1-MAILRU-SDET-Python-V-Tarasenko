import logging
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


logger = logging.getLogger('test')

MAX_RESPONSE_LENGTH = 500


class ResponseErrorException(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class InvalidLoginException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

        self.csrf_token = None

########################################################################################################################

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        logger.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = 'Got response:\n' \
                  'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n\n')
            elif logger.level == logging.DEBUG:
                logger.debug(f'{log_str}\n'
                             f'RESPONSE CONTENT: {response.text}\n\n')
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n\n')

########################################################################################################################

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True):
        url = urljoin(self.base_url, location)

        self.log_pre(method, url, headers, data, expected_status)
        response = self.session.request(method, url, headers=headers, data=data)
        self.log_post(response)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('bErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" return error "{error}"!')
            return json_response
        return response

########################################################################################################################

    def post_login(self, user, password):
        location = '/auth/'

        headers = self.post_headers

        data = {
            'login': user,
            'password': password
        }

        result = self._request('POST', location, headers=headers, data=data, jsonify=False)

        return result

########################################################################################################################

    @property
    def post_headers(self):
        return {'Content-Type': 'text/html; charset=UTF-8'}

    def get_csrftoken(self, location):
        headers = self._request('GET', location, expected_status=200, jsonify=False).headers['set-cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('csrftoken attribute not found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]
        print(headers)

        return token

########################################################################################################################

    def post_new_campaign(self):

        location = '/campaign/new/'


        csrftoken_location = '/csrf/'
        csrf_token = self.get_csrftoken(csrftoken_location)

        headers = self.post_headers
        headers['X-CSRFToken'] = f'X-CSRFToken={csrf_token}'

        return self._request('POST', location, headers=headers, data=None)

########################################################################################################################

    def post_new_segment(self):

        location = '/segments/segments_list/new/'

        headers = self.post_headers
        return self._request('POST', location, headers=headers, data=None)
