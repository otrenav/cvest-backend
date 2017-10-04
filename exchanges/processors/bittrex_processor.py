
import datetime

from .processor import Processor

# TODO: Migrate to V2
# https://bittrex.com/Api/v2.0/pub/market/
# GetTicks?marketName=BTC-WAVES&tickInterval=thirtyMin&_=1499127220008


class BittrexProcessor(Processor):

    def market_list(self, data):
        return [
            {"market": self._translate_market(market["MarketName"])}
            for market in data["result"]
        ]

    def markets(self, data):
        return [self._market(market) for market in data["result"]]

    def market(self, data):
        return self._market(data["result"][0])

    def _market(self, market):
        return {
            "market": self._translate_market(market["MarketName"]),
            "open": market["PrevDay"],
            "high": market["High"],
            "low": market["Low"],
            "close": market["Ask"],
            "volume": market["Volume"],
            "base_volume": market["BaseVolume"],
            "time_stamp_system": datetime.datetime.utcnow(),
            "time_stamp_request": market["TimeStamp"]
        }

    def balances(self, data):
        return [
            self._balance(balance)
            for balance in data["result"]
            if balance["Balance"] > 0
        ]

    def _balance(self, balance):
        return {
            "total": balance["Balance"],
            "asset": balance["Currency"],
            "available": balance["Available"],
            "address": balance["CryptoAddress"]
        }

    def _translate_market(self, string):
        pair = string.split("-")
        return "/".join([pair[1], pair[0]])
