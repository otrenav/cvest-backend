
from utilities.exceptions import InternalError

from .bittrex_requester import BittrexRequester
from .coinmarketcap_requester import CoinMarketCapRequester


def factory(name, key, secret):
    if name == "bittrex" or name == "Bittrex":
        return(BittrexRequester(key, secret))
    elif name == "coinmarketcap" or name == "CoinMarketCap":
        return(CoinMarketCapRequester())
    else:
        msg = "Unknown requester name"
        data = {"Name": name, "Key": key}
        raise InternalError(msg, data)
