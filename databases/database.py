
from abc import ABCMeta, abstractmethod


class Database(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, database, collection):
        pass

    @abstractmethod
    def write_list_of_dicts(self, listt):
        pass
