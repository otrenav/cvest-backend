
import time
import json
import hmac
import base64
import requests

from abc import ABCMeta


class Requester(metaclass=ABCMeta):

    URLS = {'GET': '', 'POST': ''}
    ACTIONS = {'GET': [], 'POST': [], 'AUTH': []}
    ENDPOINTS = {}
    PARAMS = {}
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
        return requests.request(
            self.type,
            self.url,
            headers=self.headers
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
                # TODO: This doesn't work for CoinMarketCap
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
