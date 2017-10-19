
from .constants import (
    TIMESTAMP_RECURSION_INTERVAL,
    MAX_TIMESTAMP_RECURSIONS,
    NULL_MARKET
)
from utilities.exceptions import InternalError
from utilities import TimeProcessor


class MongoSearcher:

    asset = None
    timestamp = None
    tp = TimeProcessor

    def __init__(self, assets, markets, symbols, timestamps):
        self.assets = assets
        self.markets = markets
        self.symbols = symbols
        self.timestamps = timestamps

    def get_assets(self):
        return self.assets

    def get_timestamps(self):
        return self.timestamps

    def find_previous_market(self, asset, interval):
        timestamp = self.tp.subtract_time(asset['timestamp'], interval)
        return self.find_market(asset, timestamp)

    def find_market(self, asset, timestamp, recursion_counter=0):
        if recursion_counter < MAX_TIMESTAMP_RECURSIONS:
            for market in self.markets:
                condition = (market['timestamp'] == timestamp and
                             market['symbol'] == asset['symbol'])
                if condition:
                    return market
            return self.find_market(
                asset,
                self.tp.subtract_time(timestamp, TIMESTAMP_RECURSION_INTERVAL),
                recursion_counter + 1
            )
        else:
            msg = "Maximum recursion reached for timestamp (no market found)"
            data = {
                "Recursions": recursion_counter,
                "Symbol": asset["symbol"],
                "Timestamp": timestamp
            }
            InternalError(msg, data)
            return NULL_MARKET
