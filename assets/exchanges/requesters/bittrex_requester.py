
import hashlib

from .requester import Requester


class BittrexRequester(Requester):
    URLS = {
        'GET': 'https://bittrex.com/api/v1.1',
        'POST': 'https://bittrex.com/api/v1.1'
    }
    ACTIONS = {
        'GET': ['market_list', 'markets', 'market', 'assets'],
        'POST': [],
        'AUTH': ['assets']
    }
    ENDPOINTS = {
        'market_list': '/public/getmarkets?',
        'markets': '/public/getmarketsummaries?',
        'market': '/public/getmarketsummary?',
        'assets': '/account/getbalances?'
    }
    HASH_FUNCTION = hashlib.sha512

    def _default_url_params(self):
        if self._requires_auth():
            string = '&apikey=' + self.key
            string += '&nonce=' + self.nonce
            return string
        return ''

    def _translate_market(self, string):
        pair = string.split("/")
        return "-".join([pair[1], pair[0]])

    def _setup_payload_string(self):
        self.payload_string = self.url.encode()

    def _headers_dict(self):
        return {'apisign': self.payload_signed}
