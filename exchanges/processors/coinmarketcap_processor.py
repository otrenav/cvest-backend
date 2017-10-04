
import datetime

from .processor import Processor


class CoinMarketCapProcessor(Processor):

    def markets(self, data):
        return [
            self._market(market)
            for market in data
            # Artificial restriction to
            # keep the database size down
            if (market["rank"] is not None and
                self._floatify(market["rank"]) <= 200)
        ]

    def _market(self, market):
        return {
            "id": market["id"],
            "name": market["name"],
            "rank": market["rank"],
            "symbol": market["symbol"],
            "price_btc": self._floatify(market["price_btc"]),
            "price_usd": self._floatify(market["price_usd"]),
            "volume_usd": self._floatify(market["24h_volume_usd"]),
            "market_cap_usd": self._floatify(market["market_cap_usd"]),
            "available_supply": self._floatify(market["available_supply"]),
            "total_supply": self._floatify(market["total_supply"]),
            "time_stamp": datetime.datetime.utcnow()
        }

    def _floatify(self, string):
        if string is not None:
            return float(string)
        return None

    def market_list(self, data):
        raise ValueError("Not implemented (unnecessary)")

    def market(self, data):
        raise ValueError("Not implemented (unnecessary)")

    def balances(self, data):
        raise ValueError("Not implemented (unnecessary)")
