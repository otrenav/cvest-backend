
from assets import Asset
from utilities.exceptions import ExternalError

from .wallet_requester import WalletRequester


class ARKWalletRequester(WalletRequester):

    # Alternative (community) explorers
    # https://explorer.dafty.net
    # https://explorer.ark.4miners.net
    # https://explorer.arknode.net
    # https://explorer.arkno.de
    # https://mainnet.arkexplorer.com
    # https://explorer.arkcoin.net

    # DOCS: https://github.com/ArkEcosystem/ark-explorer

    URL = "https://explorer.ark.io:8443/api/getAccount?address={address}"

    def _assets(self, resp):
        try:
            success = resp["success"]
        except KeyError as error:
            msg = "ARK response could not be parsed"
            data = {"Original error": error, "Response": resp}
            raise ExternalError(msg, data)
        assets = []
        if success:
            try:
                total = self._fix_decimals(resp["balance"])
            except KeyError as error:
                msg = "ARK response could not be parsed"
                data = {"Original error": error, "Response": resp}
                raise ExternalError(msg, data)
            if total > 0:
                assets.append(Asset({
                    "name": "Ark",
                    "symbol": "ARK",
                    "location": "Wallet",
                    "total": total
                }))
        else:
            # If not successful, we assume that the account has not
            # received any transfers yet, so it's not registered in
            # the blockchain. Therefore, we'll say it has 0 balance.
            # We create an error object to make sure the proper
            # information is printed to the screen, but we don't
            # `raise`it, so it won't interrupt the program's flow.
            msg = "ARK response indicates failure"
            data = {"Response": resp}
            ExternalError(msg, data)
        return assets

    def _fix_decimals(self, number_str):
        """Need to ensure 8 decimal places in the number we get from the API.
        """
        return self._floatify(number_str) / (10 ** 8)
