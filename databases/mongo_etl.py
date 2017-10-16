
from datetime import datetime, timedelta


class MongoETL:

    def assets_time_series(self, assets, markets, symbols, timestamps):
        return [
            self._observation(
                timestamp,
                self._values_at_timestamp(timestamp, assets, markets)
            )
            for timestamp in timestamps
        ]

    def assets_current_status(self, time_series):
        # Is in ascending order
        last = time_series[-1]
        return {
            'timestamp': last['timestamp'],
            'btc': last['btc'],
            'usd': last['usd'],
            'btc_1h': self._percent_change(last, time_series, '1h', 'btc'),
            'btc_1d': self._percent_change(last, time_series, '1d', 'btc'),
            'btc_1w': self._percent_change(last, time_series, '1w', 'btc'),
            'btc_1m': self._percent_change(last, time_series, '1m', 'btc'),
            'btc_1y': self._percent_change(last, time_series, '1y', 'btc'),
            'usd_1h': self._percent_change(last, time_series, '1h', 'usd'),
            'usd_1d': self._percent_change(last, time_series, '1d', 'usd'),
            'usd_1w': self._percent_change(last, time_series, '1w', 'usd'),
            'usd_1m': self._percent_change(last, time_series, '1m', 'usd'),
            'usd_1y': self._percent_change(last, time_series, '1y', 'usd')
        }

    def assets_balance(self):
        return []

    def _percent_change(self, last, time_series, interval, base):
        timestamp = last['timestamp']
        since = self._subtract_time(timestamp, interval)
        time_series = [obs for obs in time_series if obs['timestamp'] >= since]
        first = time_series[0]
        return ((last[base] - first[base]) / first[base]) * 100

    def _subtract_time(self, timestamp, interval):
        date_time = datetime.strptime(timestamp, "%Y-%m-%d-%H-%M")
        if interval == '1h':
            date_time -= timedelta(hours=1)
        elif interval == '1d':
            date_time -= timedelta(days=1)
        elif interval == '1w':
            date_time -= timedelta(weeks=1)
        elif interval == '1m':
            date_time -= timedelta(weeks=4)
        elif interval == '1y':
            date_time -= timedelta(weeks=52)
        return date_time.strftime("%Y-%m-%d-%H-%M")

    def _values_at_timestamp(self, timestamp, assets, markets):
        values = [
            self._values_for_asset_at_timestamp(asset, timestamp, markets)
            for asset in assets if asset['timestamp'] == timestamp
        ]
        return {
            'btc': sum([v['btc'] for v in values]),
            'usd': sum([v['usd'] for v in values])
        }

    def _values_for_asset_at_timestamp(self, asset, timestamp, markets):
        for market in markets:
            condition = (market['timestamp'] == timestamp and
                         market['symbol'] == asset['symbol'])
            if condition:
                return {
                    'btc': self._total_value(asset, market, 'btc'),
                    'usd': self._total_value(asset, market, 'usd')
                }
        return {'btc': 0, 'usd': 0}

    def _total_value(self, asset, market, base):
        total = asset['total']
        value = market['price_{}'.format(base)]
        return self._floatify(total) * self._floatify(value)

    def _floatify(self, string):
        if string is not None:
            return float(string)
        return 0

    def _observation(self, timestamp, values):
        return {
            'timestamp': timestamp,
            'btc': values['btc'],
            'usd': values['usd']
        }

    def _asset(self):
        return {
            'timestamp': None,
            'name': None,
            'symbol': None,
            'total': None,
            'available': None,
            'btc': None,
            'usd': None,
            '1h': None,
            '1d': None,
            '1w': None,
            '1m': None,
            '1y': None,
            'note': None
        }
