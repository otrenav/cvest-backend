
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
            "symbol": market["symbol"],
            "price_btc": self._floatify(market["price_btc"]),
            "price_usd": self._floatify(market["price_usd"]),
            "volume_usd": self._floatify(market["24h_volume_usd"]),
            "market_cap_usd": self._floatify(market["market_cap_usd"]),
            "available_supply": self._floatify(market["available_supply"]),
            "total_supply": self._floatify(market["total_supply"]),
            "timestamp": None
        }

    def market_list(self, data):
        pass

    def market(self, data):
        pass

    def assets(self, data):
        pass
