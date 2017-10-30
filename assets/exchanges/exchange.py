
from .requesters.factory import factory as requester_factory
from .processors.factory import factory as processor_factory


class Exchange:

    def __init__(self, name='', key='', secret=''):
        self.name = name
        self.requester = requester_factory(name, key, secret)
        self.processor = processor_factory(name)

    def update_markets(self, timestamp, db):
        data = self._insert_timestamp(timestamp, self.markets())
        return db.write_markets(self.name, data)

    def market_list(self):
        data = self.requester.request('market_list')
        return self.processor.process('market_list', data)

    def markets(self):
        data = self.requester.request('markets')
        return self.processor.process('markets', data)

    def market(self, market):
        params = {'market': market}
        data = self.requester.request('market', params)
        return self.processor.process('market', data)

    def assets(self):
        data = self.requester.request('assets')
        return self.processor.process('assets', data)

    def _insert_timestamp(self, timestamp, markets):
        for market in markets:
            market.update({"timestamp": timestamp})
        return markets
