
from ..assets_container import AssetsContainer

from .requesters import factory


class Wallet(AssetsContainer):

    def __init__(self, params):
        self.requester = factory(params["symbol"], params["address"])
        self.container = params["symbol"]
        self.user_id = params["user_id"]
        self.address = params["address"]
        self.symbol = params["symbol"]

    def _get_assets(self):
        return self._insert_non_wallet_data(self.requester.assets())

    def _insert_non_wallet_data(self, assets):
        for asset in assets:
            asset.copy_total_to_available()
            asset.set_address(self.address)
        return assets
