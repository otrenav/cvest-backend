
from assets import Asset
from utilities.exceptions import CVESTExternalError

from .wallet_requester import WalletRequester


class LTCWalletRequester(WalletRequester):

    # DOCS: https://chainz.cryptoid.info/api.dws

    URL = ("https://chainz.cryptoid.info/ltc/api.dws?" +
           "q=getbalance&a={address}")

    def _assets(self, resp):
        try:
            total = self._floatify(resp)
        except KeyError as error:
            msg = "LTC response could not be parse"
            data = {"Original error": error, "Response": resp}
            raise CVESTExternalError(msg, data)
        assets = []
        if total > 0:
            assets.append(Asset({
                "name": "Litecoin",
                "symbol": "LTC",
                "location": "Wallet",
                "total": total
            }))
        return assets
