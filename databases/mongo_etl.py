
from utilities import TextProcessor


class MongoETL:

    searcher = None
    tp = TextProcessor

    def assets_time_series(self, searcher):
        self.searcher = searcher
        return self._time_series()

    def _time_series(self):
        return [
            {
                'timestamp': timestamp,
                'assets': [
                    self._build_asset(asset, timestamp)
                    for asset in self.searcher.get_assets()
                    if asset['timestamp'] == timestamp
                ]
            }
            for timestamp in self.searcher.get_timestamps()
        ]

    def _build_asset(self, asset, timestamp):
        market = self.searcher.find_market(asset, timestamp)
        return {
            # 'id': str(asset['_id']),
            'name': asset['name'],
            'symbol': asset['symbol'],
            'location': asset['location'],
            'total': asset['total'],
            'available': asset['available'],
            'btc': self._total_value(asset, market, 'btc'),
            'btc_1h': self._percent_change(asset, market, '1h', 'btc'),
            'btc_1d': self._percent_change(asset, market, '1d', 'btc'),
            'btc_1w': self._percent_change(asset, market, '1w', 'btc'),
            'btc_1m': self._percent_change(asset, market, '1m', 'btc'),
            'btc_1y': self._percent_change(asset, market, '1y', 'btc'),
            'usd': self._total_value(asset, market, 'usd'),
            'usd_1h': self._percent_change(asset, market, '1h', 'usd'),
            'usd_1d': self._percent_change(asset, market, '1d', 'usd'),
            'usd_1w': self._percent_change(asset, market, '1w', 'usd'),
            'usd_1m': self._percent_change(asset, market, '1m', 'usd'),
            'usd_1y': self._percent_change(asset, market, '1y', 'usd'),
            'address': asset['address']
        }

    def _total_value(self, asset, market, base):
        total = asset['total']
        price = market['price_{}'.format(base)]
        if price is None:
            return None
        return self.tp.floatify(total) * self.tp.floatify(price)

    def _percent_change(self, asset, market_2, interval, base):
        base = "price_{}".format(base)
        market_1 = self.searcher.find_previous_market(asset, interval)
        if market_1[base] is None:
            return None
        return ((market_2[base] - market_1[base]) / market_1[base]) * 100
