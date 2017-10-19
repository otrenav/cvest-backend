
from utilities.exceptions import InternalError

from .bittrex_processor import BittrexProcessor
from .coinmarketcap_processor import CoinMarketCapProcessor


def factory(name):
    if name == "bittrex" or name == "Bittrex":
        return(BittrexProcessor())
    elif name == "coinmarketcap" or name == "CoinMarketCap":
        return(CoinMarketCapProcessor())
    else:
        msg = "Unknown processor"
        data = {"Processor": name}
        raise InternalError(msg, data)
