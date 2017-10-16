
from assets import Asset
from utilities.exceptions import CVESTExternalError

from .wallet_requester import WalletRequester


class NEOWalletRequester(WalletRequester):

    # DOCS: https://github.com/CityOfZion/neon-wallet-db

    URL = "https://api.neonwallet.com/v2/address/balance/{address}"

    def _assets(self, resp):
        try:
            total = self._floatify(resp["NEO"]["balance"])
        except KeyError as error:
            msg = "NEO response could not be parsed"
            data = {"Original error": error, "Response": resp}
            raise CVESTExternalError(msg, data)
        assets = []
        if total > 0:
            assets.append(Asset({
                "name": "Neo",
                "symbol": "NEO",
                "location": "Wallet",
                "total": total
            }))
        try:
            total = self._floatify(resp["GAS"]["balance"])
        except KeyError as error:
            msg = "GAS response could not be parsed"
            data = {"Original error": error, "Response": resp}
            raise CVESTExternalError(msg, data)
        if total > 0:
            assets.append(Asset({
                "name": "Gas",
                "symbol": "GAS",
                "location": "Wallet",
                "total": total
            }))
        return assets
