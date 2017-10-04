
import logging

from .bittrex_requester import BittrexRequester
from .coinmarketcap_requester import CoinMarketCapRequester

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def factory(name, key, secret):
    if name == "Bittrex":
        return(BittrexRequester(key, secret))
    elif name == "CoinMarketCap":
        return(CoinMarketCapRequester())
    else:
        msg = "CVEST: unknown requester: {}".format(name)
        LOGGER.critical(msg)
        raise ValueError(msg)
