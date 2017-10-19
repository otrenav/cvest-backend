
import requests

from assets import Asset
from utilities.exceptions import ExternalError

from .wallet_requester import WalletRequester

#
# TODO: If errors continue, randomly select server
#


class IOTAWalletRequester(WalletRequester):

    # IOTA nodes. Use HTTPS if available!
    URL = "http://iota.bitfinex.com:80"
    # URL = "http://service.iotasupport.com:14265"
    # URL = "http://node01.iotatoken.nl:14265"
    # URL = "http://node02.iotatoken.nl:14265"
    # URL = "http://node03.iotatoken.nl:15265"
    # URL = "http://mainnet.necropaz.com:14500"
    # URL = "http://5.9.137.199:14265"
    # URL = "http://5.9.118.112:14265"
    # URL = "http://5.9.149.169:14265"
    # URL = "http://88.198.230.98:14265"
    # URL = "http://176.9.3.149:14265"
    # URL = "http://node.lukaseder.de:14265"
    # URL = "http://iota.preissler.me:80"
    # URL = "http://iotanode.prizziota.com:80"
    # URL = "https://iota.preissler.me:443"
    # URL = "https://iotanode.prizziota.com:443"

    def _request(self):
        data = ('{"command": "getBalances", "threshold": 100, ' +
                '"addresses": [{address}]'.format(address=self.address) + '}')
        try:
            resp = requests.post(url=self.URL, data=data).json()
        except KeyError as error:
            # TODO: This is not a `KeyError`. What is it?
            msg = "IOTA's JSON response could not be parsed"
            data = {"Original error": error, "URL": self.URL, "Data": data}
            raise ExternalError(msg, data)
        return resp

    def _assets(self, resp):
        try:
            total = self._floatify(resp["balances"][0])
        except KeyError as error:
            msg = "IOTA response could not be parsed"
            data = {"Original error": error, "Response": resp}
            raise ExternalError(msg, data)
        assets = []
        if total > 0:
            assets.append(Asset({
                "name": "IOTA",
                "symbol": "MIOTA",
                "location": "Wallet",
                # NOTE: We follow CoinMarketCap's convention of using MIOTA
                #       as the base unit, which is equivalent to 1,000,000
                #       IOTAs. This is to simplify price calculations.
                "total": total / 1000000
            }))
        return assets
