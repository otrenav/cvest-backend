
from .requester import Requester


class CoinMarketCapRequester(Requester):
    URLS = {
        'GET': 'https://api.coinmarketcap.com/v1/',
        'POST': ''
    }
    ACTIONS = {
        'GET': ['market_list', 'markets', 'market'],
        'POST': [],
        'AUTH': []
    }
    ENDPOINTS = {
        # 'market_list': 'ticker/',
        'markets': 'ticker/'
        # 'market': 'ticker/',
    }
    PARAMS = {'market': 'market'}
    HASH_FUNCTION = None
