
from utilities.exceptions import ExternalError

from .constants import KNOWN_ASSETS, ERC20_TOKENS


class Asset:

    def __init__(self, params):
        self.name = params.get("name", self._default_name(params["symbol"]))
        self.available = params.get("available", None)
        self.user_id = params.get("user_id", None)
        self.address = params.get("address", None)
        self.location = params["location"]
        self.symbol = params["symbol"]
        self.total = params["total"]
        self.timestamp = None

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def set_address(self, address):
        self.address = address

    def copy_total_to_available(self):
        self.available = self.total

    def _default_name(self, symbol):
        if symbol in KNOWN_ASSETS.keys():
            return KNOWN_ASSETS.get(symbol, symbol)
        if symbol in ERC20_TOKENS.keys():
            return ERC20_TOKENS[symbol]["name"]
        data = {"Symbol": symbol}
        msg = "Symbol not in KNOWN_ASSETS or ERC20_TOKENS"
        raise ExternalError(msg, data)
