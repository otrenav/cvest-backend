
from .requester import Requester


class CoinMarketCapRequester(Requester):
    URLS = {
        'GET': 'https://api.coinmarketcap.com/v1/',
        'POST': ''
    }
    ACTIONS = {
        'GET': ['markets'],
        'POST': [],
        'AUTH': []
    }
    ENDPOINTS = {
        'markets': 'ticker/'
    }
