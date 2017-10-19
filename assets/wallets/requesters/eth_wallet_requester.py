
import requests

# from decimal import Decimal

from assets import Asset, ERC20_TOKENS
from utilities.exceptions import ExternalError

from .wallet_requester import WalletRequester


class ETHWalletRequester(WalletRequester):

    # NOTE: Ethplorer had a nicer API, but has restricting usage limits
    # DOCS: https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API
    # URL = "https://api.ethplorer.io/getAddressInfo/{address}?apiKey=freekey"

    # NOTE: The most "professional" option is EtherScan, but you need
    #        to parse the results yourself.
    # DOCS: https://etherscan.io/apis
    # URL = ("https://api.etherscan.io/api?module=account&action=balance" +
    #        "&address={address}&tag=latest&apikey={key}")
    # KEY = "EVCWMGVFCF3NFZ85MYV38I2KJDCHNBW4N8"

    # NOTE: The 2nd best API seems to be TokenBalance, but we need to
    #       iterate over the possible token contracts, which is not great
    # DOCS: https://tokenbalance.com/documentation
    URL = "https://api.tokenbalance.com/token/{token_contract}/{address}"

    # def _request(self):
    #     # NOTE: This is for the Ethplorer API
    #     url = self.URL.format(address=self.address, key=self.KEY)
    #     try:
    #         resp = requests.get(url).json()
    #     except KeyError as error:
    #         # TODO: This is not a `KeyError`. What is it?
    #         msg = "ETH's JSON response could not be parsed"
    #         data = {"Original error": error, "URL": url}
    #         raise ExternalError(msg, data)
    #     return resp

    def _request(self):
        """Get data for each token and put it into a single resp object.
        The data for ETH does not have to be requested separately because
        every token request includes the ETH balance inside.
        """
        resps = []
        for symbol in ERC20_TOKENS.keys():
            print("        [+] {}".format(symbol))
            url = self.URL.format(
                token_contract=ERC20_TOKENS[symbol]["contract"],
                address=self.address
            )
            try:
                resp = requests.get(url).json()
            except KeyError as error:
                # TODO: This is not a `KeyError`. What is it?
                msg = "ERC-20 TOKEN's JSON response could not be parsed"
                data = {"Original error": error, "Token": symbol}
                raise ExternalError(msg, data)
            resps.append(resp)
        return resps

    def _assets(self, resps):
        try:
            total = self._floatify(resps[0]["eth_balance"])
        except KeyError as error:
            msg = "ETH response could not be parsed"
            data = {"Original error": error, "Response": resps[0]}
            raise ExternalError(msg, data)
        assets = []
        if total > 0:
            assets.append(Asset({
                "name": "Ether",
                "symbol": "ETH",
                "location": "Wallet",
                "total": total
            }))
        for resp in resps:
            try:
                total = self._floatify(resp["balance"])
            except KeyError as error:
                # If we did not fail earlier with the ETH asset, then there's
                # the possibility that we got a valid response and we just
                # have unexpected data for a token. In that case, we don't
                # want to loose the information we got correctly, so we
                # don't interrupt the program's flow by `raising` the error.
                msg = "ERC-20 TOKEN response could not be parsed"
                data = {"Original error": error, "Response": resp}
                ExternalError(msg, data)
            if total > 0:
                assets.append(Asset({
                    "name": ERC20_TOKENS[resp["symbol"]]["name"],
                    "symbol": resp["symbol"],
                    "location": "Wallet",
                    "total": total
                }))
        return assets

    # def _assets(self, resp):
    #     # NOTE: This is for the Ethplorer API
    #     try:
    #         eth = Asset({
    #             "name": "Ether",
    #             "symbol": "ETH",
    #             "location": "Wallet",
    #             "total": self._floatify(resp["ETH"]["balance"])
    #         })
    #     except KeyError as error:
    #         msg = "ETH response could not be parsed"
    #         data = {"Original error": error, "Response": resp}
    #         raise ExternalError(msg, data)
    #     assets = [eth]
    #     for token in resp.get("tokens", []):
    #         try:
    #             token = Asset({
    #                 "location": "Wallet",
    #                 "symbol": token["tokenInfo"]["symbol"],
    #                 "total": self._fix_decimals(
    #                     token["tokenInfo"]["decimals"],
    #                     token["balance"]
    #                 )
    #             })
    #         except KeyError as error:
    #             # If we did not fail earlier with the ETH asset, then there's
    #             # the possibility that we got a valid response and we just
    #             # have unexpected data for a token. In that case, we don't
    #             # want to loose the information we got correctly, so we
    #             # don't interrupt the program's flow by `raising` the error.
    #             msg = "ERC-20 TOKEN response could not be parsed"
    #             data = {"Original error": error, "Response": resp}
    #             ExternalError(msg, data)
    #         assets += [token]
    #     return assets

    # def _fix_decimals(self, decimals, num_str):
    #     """Tokens can have different number of decimal places. If the API being
    #     used does not handle the decimal places conversion for us (the current
    #     one does not), then we need to handle it ourselves. Most tokens use 18
    #     decimal places, so we'll use that a the default.
    #     """
    #     times_to_move = -Decimal(num_str).as_tuple().exponent - int(decimals)
    #     return self._floatify(num_str) * 10 ** times_to_move
