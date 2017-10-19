
from utilities.exceptions import InternalError
from assets import ERC20_TOKENS

from .btc_wallet_requester import BTCWalletRequester
from .eth_wallet_requester import ETHWalletRequester
from .ltc_wallet_requester import LTCWalletRequester
from .neo_wallet_requester import NEOWalletRequester
from .ark_wallet_requester import ARKWalletRequester
from .iota_wallet_requester import IOTAWalletRequester


def factory(symbol, address):
    if symbol == "BTC":
        return BTCWalletRequester(address)
    elif symbol == "ETH" or symbol in ERC20_TOKENS.keys():
        return ETHWalletRequester(address)
    elif symbol == "LTC":
        return LTCWalletRequester(address)
    elif symbol == "NEO":
        return NEOWalletRequester(address)
    elif symbol == "ARK":
        return ARKWalletRequester(address)
    elif symbol == "MIOTA":
        return IOTAWalletRequester(address)
    else:
        msg = "Unknown symbol"
        data = {"Symbol": symbol, "Address": address}
        raise InternalError(msg, data)
