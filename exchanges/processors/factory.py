
import logging

from .bittrex_processor import BittrexProcessor
from .coinmarketcap_processor import CoinMarketCapProcessor

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def factory(name):
    if name == "Bittrex":
        return(BittrexProcessor())
    elif name == "CoinMarketCap":
        return(CoinMarketCapProcessor())
    else:
        msg = "CVEST: unknown processor: {}".format(name)
        LOGGER.critical(msg)
        raise ValueError(msg)
