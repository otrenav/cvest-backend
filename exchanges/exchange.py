
from abc import ABCMeta

from .requesters.factory import factory as requester_factory
from .processors.factory import factory as processor_factory


class Exchange(metaclass=ABCMeta):

    def __init__(self, name='', key='', secret=''):
        self.name = name
        self.requester = requester_factory(name, key, secret)
        self.processor = processor_factory(name)

    def market_list(self):
        data = self.requester.request('market_list')
        data = self.processor.process('market_list', data)
        return data

    def markets(self):
        data = self.requester.request('markets')
        data = self.processor.process('markets', data)
        return data

    def market(self, market):
        params = {'market': market}
        data = self.requester.request('market', params)
        data = self.processor.process('market', data)
        return data

    def balances(self):
        data = self.requester.request('balances')
        data = self.processor.process('balances', data)
        return data
