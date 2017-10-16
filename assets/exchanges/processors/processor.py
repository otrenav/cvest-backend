
from abc import ABCMeta, abstractmethod


class Processor(metaclass=ABCMeta):

    def process(self, action, data):
        return getattr(self, action)(data)

    @abstractmethod
    def market_list(self, data):
        pass

    @abstractmethod
    def markets(self, data):
        pass

    @abstractmethod
    def market(self, data):
        pass

    @abstractmethod
    def assets(self, data):
        pass

    def _floatify(self, string):
        if string is not None:
            return float(string)
        return None
