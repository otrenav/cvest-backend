
import time
import json
import hmac
import base64
import urllib3
import requests

from pprint import pprint
from abc import ABCMeta

# NOTE: If we remove the `verify=False` parameter from the `requests.request()`
# function, we are getting an error when working with a specific wallet
# requester (TODO: Verify which one). To avoid that, we disable the
# verification, but we should also disable the warning to avoid having the
# screen cluttered with them.
#
urllib3.disable_warnings()


class Requester(metaclass=ABCMeta):

    URLS = {'GET': '', 'POST': ''}
    ACTIONS = {'GET': [], 'POST': [], 'AUTH': []}
    ENDPOINTS = {}
    PARAMS = {'market': 'market'}
    HASH_FUNCTION = None

    def __init__(self, key='', secret=''):
        self.key = key
        self.secret = secret
        self.payload_string = ''
        self.payload = {}
        self.headers = {}
        self.params = {}
        self.action = ''
        self.type = ''
        self.url = ''

    def request(self, action, params={}):
        self.action = action
        self.params = params
        self._setup_url()
        self._setup_headers()

        # print('1' * 50)
        # print(self.type)
        # print(self.url)
        # pprint(self.headers)
        # print('1' * 50)

        return requests.request(
            self.type,
            self.url,
            headers=self.headers,
            verify=False
        ).json()

    def _setup_url(self):
        if self.action in self.ACTIONS['GET']:
            self.type = 'GET'
            self.url = self._get_url()
        else:
            self.type = 'POST'
            self.url = self._post_url()

    def _get_url(self):
        return '{}{}{}'.format(
            self.URLS[self.type],
            self.ENDPOINTS[self.action],
            self._url_params()
        )

    def _post_url(self):
        return '{}{}{}'.format(
            self.URLS[self.type],
            self.ENDPOINTS[self.action],
            self._url_params()
        )

    def _url_params(self):
        string = self._default_url_params()
        for name, param in self.params.items():
            if param is not None:
                if name == 'market':
                    param = self._translate_market(param)
                string += '&' + self.PARAMS[name] + '=' + param
        return string

    def _default_url_params(self):
        return ''

    def _translate_market(self, string):
        return string

    def _setup_headers(self):
        if not self._requires_auth():
            self.headers = {}
        else:
            self._setup_payload_dict()
            self._setup_payload_string()
            self._setup_payload_signed()
            self.headers = self._headers_dict()

    def _setup_payload_dict(self):
        self.payload = {}

    def _setup_payload_string(self):
        json_string = json.dumps(self.payload).encode()
        self.payload_string = base64.standard_b64encode(json_string)

    def _setup_payload_signed(self):
        self.payload_signed = hmac.new(
            self.secret.encode(),
            self.payload_string,
            self.HASH_FUNCTION
        ).hexdigest()

    def _headers_dict(self):
        return {}

    def _requires_auth(self):
        return self.action in self.ACTIONS['AUTH']

    @property
    def nonce(self):
        return str(int(time.time() * 1000000))
