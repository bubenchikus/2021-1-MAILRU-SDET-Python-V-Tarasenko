from urllib.parse import urljoin
import json_lab
import os
import allure

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
        self.csrf_token = None
        self.mc_token = None
        self.sdcs_token = None
        self.current_campaign_id = None
        self.current_segment_id = None

    def _request(self, method, location, headers=None, data=None, files=None, cookies=None, expected_status=200,
                 jsonify=True, loc_join=True):

        if loc_join:
            url = urljoin(self.base_url, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, data=data, files=files, cookies=cookies)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}":!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            return json_response

        return response

    @allure.step('Getting CSRF token')
    def get_csrf_token(self):
        headers = self._request('GET', '/csrf/', jsonify=False).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]

        return token

    @property
    def post_headers(self):
        return {'X-CSRFToken': self.csrf_token}

    @allure.step('Authorizing')
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

        result = self._request('POST', location=location, headers=headers, data=data, jsonify=False, loc_join=False)

        try:
            r = result.request
            reverse_request_cookies = r.headers['Cookie'].split(';')
        except Exception as e:
            raise InvalidLoginException(e)

        self.csrf_token = self.get_csrf_token()
        self.mc_token = [c for c in reverse_request_cookies if 'mc' in c][0].split('=')[-1]
        self.sdcs_token = [c for c in reverse_request_cookies if 'sdcs' in c][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({'mc': self.mc_token, 'sdcs': self.sdcs_token,
                                                    'csrftoken': self.csrf_token})

        return result

    def post_url_get_id(self, url):

        location = f'https://target.my.com/api/v1/urls/?url={url}'
        cookies = self.session.cookies
        headers = self.post_headers
        data = {}

        result = self._request('GET', location=location, headers=headers, data=data, cookies=cookies)

        url_id = result['id']

        return url_id

    @allure.step('Generating url ids')
    def get_all_urls_ids(self, slides_num):

        urls_ids = []

        for i in range(slides_num):
            url = json_lab.generate_url()
            urls_ids.append(self.post_url_get_id(url))
        print(urls_ids)
        return urls_ids

    def post_picture_get_id(self, path):

        location = 'api/v2/content/static.json'
        cookies = self.session.cookies
        headers = self.post_headers
        files = {"file": open(path, 'rb')}
        data = {}

        result = self._request('POST', location=location, headers=headers, data=data, files=files, cookies=cookies)

        img_id = result['id']

        return img_id

    @allure.step('Generating pic ids')
    def get_all_pictures_ids(self):

        path = os.path.join(os.path.abspath(__file__), '../..', 'files')
        path = os.path.abspath(path)

        ids_600 = []
        id_256 = None
        ids_no_crop = []

        for file in os.listdir(path):
            path1 = os.path.join(path, file)
            if file.endswith('600.jpg'):
                ids_600.append(self.post_picture_get_id(path1))
            elif file.endswith('256.jpg'):
                id_256 = self.post_picture_get_id(path1)
            else:
                ids_no_crop.append(self.post_picture_get_id(path1))

        return ids_600, id_256

    @allure.step('Creating campaign')
    def post_create_campaign(self):

        location = '/api/v2/campaigns.json'
        cookies = self.session.cookies
        headers = self.post_headers

        slides_num = 3
        slides_urls = self.get_all_urls_ids(slides_num + 1)
        ids_600, id_256 = [self.get_all_pictures_ids()[i] for i in [0, 1]]
        data = json_lab.configure_and_return_campaign_json(slides_urls, ids_600, id_256)

        result = self._request('POST', location=location, data=data, headers=headers, cookies=cookies)

        try:
            self.current_campaign_id = result['id']
        except CampaignCreationError:
            print('No id attribute found')

        return result

    @allure.step('Deleting campaign')
    def delete_campaign(self):

        location = f'/api/v2/campaigns/{self.current_campaign_id}.json'
        cookies = self.session.cookies
        headers = self.post_headers
        data = {}

        result = self._request('DELETE', location=location, headers=headers, data=data, cookies=cookies,
                               expected_status=204, jsonify=False)

        return result

    @allure.step('Creating segment')
    def post_create_segment(self):

        location = '/api/v2/remarketing/segments.json'
        cookies = self.session.cookies
        headers = self.post_headers
        data = json_lab.configure_and_return_segment_json()

        result = self._request('POST', location=location, headers=headers, data=data,
                               cookies=cookies, expected_status=200, jsonify=True)

        try:
            self.current_segment_id = result['id']
        except SegmentCreationError:
            print('No id attribute found')

        return result

    @allure.step('Deleting segment')
    def delete_segment(self):
        location = f'/api/v2/remarketing/segments/{self.current_segment_id}.json'

        cookies = self.session.cookies
        headers = {'X-CSRFToken': self.csrf_token}

        data = {}

        result = self._request('DELETE', location=location, headers=headers, data=data,
                               cookies=cookies, expected_status=204, jsonify=False)

        return result

    def get_ids_page(self, location):

        location = location
        cookies = self.session.cookies
        headers = self.post_headers
        data = {}

        result = self._request('GET', location=location, data=data, headers=headers, cookies=cookies)

        return result

    @allure.step('Getting all active campaigns ids')
    def get_campaigns_ids(self):

        result = self.get_ids_page('/api/v2/banners/delivery.json?_campaign_status=active')

        ids = []
        for i in result['delivering'], result['not_delivering'], result['pending']:
            for j in i:
                ids.append(j['campaign_id'])

        return ids

    @allure.step('Getting all active segments ids')
    def get_segments_ids(self):
        result = self.get_ids_page('/api/v2/remarketing/segments.json')

        ids = []
        for i in result['items']:
            ids.append(i['id'])
        return ids
