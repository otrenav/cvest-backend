
import requests

from utilities.exceptions import CVESTInternalError

from abc import ABCMeta, abstractmethod
from pprint import pprint


class WalletRequester(metaclass=ABCMeta):

    URL = ""

    def __init__(self, address):
        self.address = address

    def assets(self):
        return self._assets(self._request())

    def _request(self):
        url = self.URL.format(address=self.address)
        try:
            data = requests.get(url).json()
        except ValueError as error:
            data = {"URL": url}
            msg = "Could not parse JSON response"
            raise CVESTInternalException(msg, data)
        return data

    @abstractmethod
    def _assets(self, resp):
        """Parse the assets gotten from the request to generate an appropriate
        list of `Asset` instances. It must be a list to solve the general case
        where a single wallet can contain multiple assets (Ethereum).

        This function is highly dependent on the response structure we get from
        the API being used to get the wallet's assets. It needs to parse
        accordingly.
        """
        pass

    def _floatify(self, string):
        if string is not None:
            return float(string)
        return None
