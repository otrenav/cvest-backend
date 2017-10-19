
from assets import Asset
from utilities.exceptions import ExternalError

from .wallet_requester import WalletRequester


class BTCWalletRequester(WalletRequester):

    # DOCS: https://chainz.cryptoid.info/api.dws

    URL = ("https://chainz.cryptoid.info/btc/api.dws?" +
           "q=getbalance&a={address}")

    def _assets(self, resp):
        try:
            total = self._floatify(resp)
        except KeyError as error:
            msg = "BTC response could not be parsed"
            data = {"Original error": error, "Response": resp}
            raise ExternalError(msg, data)
        assets = []
        if total > 0:
            assets.append(Asset({
                "name": "Bitcoin",
                "symbol": "BTC",
                "location": "Wallet",
                "total": total
            }))
        return assets
