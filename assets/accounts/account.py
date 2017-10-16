
from assets.exchanges import Exchange

from ..assets_container import AssetsContainer


class Account(AssetsContainer):

    def __init__(self, params):
        self.container = params["exchange"].upper()
        self.user_id = params["user_id"]
        self.secret = params["secret"]
        self.key = params["key"]
        self.exchange = Exchange(
            params["exchange"],
            params["key"],
            params["secret"]
        )

    def _get_assets(self):
        return self.exchange.assets()
