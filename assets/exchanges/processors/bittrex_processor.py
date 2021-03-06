
import datetime

from assets import Asset
from utilities.exceptions import ExternalError

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

    def assets(self, resp):
        if resp["success"]:
            return [
                self._asset(asset)
                for asset in resp["result"]
                if asset["Balance"] is not None and asset["Balance"] > 0
            ]
        else:
            data = {'Response': resp}
            msg = "Could not process Bittrex response"
            raise ExternalError(msg, data)

    def _asset(self, asset):
        return Asset({
            "address": asset["CryptoAddress"],
            "available": asset["Available"],
            "symbol": asset["Currency"],
            "total": asset["Balance"],
            "location": "Bittrex",
        })

    def _translate_market(self, string):
        pair = string.split("-")
        return "/".join([pair[1], pair[0]])
