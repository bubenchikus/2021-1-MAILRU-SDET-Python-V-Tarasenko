import os
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


class InvalidLoginException(Exception):
    pass

class CampaignCreationError(Exception):
    pass

class SegmentCreationError(Exception):
    pass


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, base_url):

        self.base_url = base_url
        self.session = requests.Session()
        self.z_token = None
        self.csrf_token = None
        self.mc_token = None
        self.mrcu_token = None
        self.sdcs_token = None
        self.current_campaign_id = None
        self.current_segment_id = None

    def _request(self, method, location, headers=None, data=None, cookies=None, expected_status=200,
                 jsonify=True, loc_join=False):

        if loc_join:
            url = urljoin(self.base_url, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, data=data, cookies=cookies)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}":!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            return json_response

        return response

    def get_csrf_token(self):
        headers = self._request('GET', 'https://target.my.com/csrf/', jsonify=False).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]

        return token

    def post_login(self, user, password):

        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': user,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        result = self._request('POST', location=location, headers=headers, data=data, jsonify=False)

        try:
            response_cookies = result.headers['set-cookie'].split(';')
        except Exception as e:
            raise InvalidLoginException(e)

        new_z_token = [c for c in response_cookies if 'z' in c][0].split('=')[-1]
        self.z_token = new_z_token

        r = result.request
        reverse_request_cookies = r.headers['Cookie'].split(';')

        self.csrf_token = self.get_csrf_token()
        self.mc_token = [c for c in reverse_request_cookies if 'mc' in c][0].split('=')[-1]
        self.mrcu_token = [c for c in reverse_request_cookies if 'mrcu' in c][0].split('=')[-1]
        self.sdcs_token = [c for c in reverse_request_cookies if 'sdcs' in c][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({'z': self.z_token, 'mc': self.mc_token, 'mrcu': self.mrcu_token,
                                                    'sdcs': self.sdcs_token, 'csrftoken': self.csrf_token})

        return result

    def post_create_campaign(self):

        location = 'https://target.my.com/api/v2/campaigns.json'

        cookies = self.session.cookies

        headers = {'X-CSRFToken': self.csrf_token}

        file_path = os.path.abspath(__file__)
        txt_path = os.path.join(file_path, '../../..', 'code/campaign.txt')
        txt_path = os.path.abspath(txt_path)
        with open(txt_path, 'r') as f:
            data = f.readline()

        result = self._request('POST', location=location, data=data, headers=headers,
                               cookies=cookies, expected_status=200, jsonify=True)
        try:
            self.current_campaign_id = result['id']
        except CampaignCreationError:
            print('No id attribute found')

        return result

    def post_delete_campaign(self):

        location = 'https://target.my.com/api/v2/campaigns/mass_action.json'

        cookies = self.session.cookies
        headers = {'X-CSRFToken': self.csrf_token}
        data = [{'id': self.current_campaign_id, 'status': 'deleted'}]

        result = self._request('POST', location=location, headers=headers, data=data,
                               cookies=cookies, expected_status=204, jsonify=False)

        return result

    def post_create_segment(self):

        location = 'https://target.my.com/api/v2/remarketing/segments.json'

        cookies = self.session.cookies
        headers = {'X-CSRFToken': self.csrf_token}

        file_path = os.path.abspath(__file__)
        txt_path = os.path.join(file_path, '../../..', 'code/segment.txt')
        txt_path = os.path.abspath(txt_path)
        with open(txt_path, 'r') as f:
            data = f.readline()

        result = self._request('POST', location=location, headers=headers, data=data,
                               cookies=cookies, expected_status=200, jsonify=True)

        try:
            self.current_segment_id = result['id']
        except SegmentCreationError:
            print('No id attribute found')

        return result

    def post_delete_segment(self):
        location = 'https://target.my.com/api/v1/remarketing/mass_action/delete.json'

        cookies = self.session.cookies
        headers = {'X-CSRFToken': self.csrf_token}

        data = [{'source_id': self.current_segment_id, 'source_type': 'segment'}]

        result = self._request('POST', location=location, headers=headers, data=data,
                               cookies=cookies, expected_status=200, jsonify=True)

        return result
