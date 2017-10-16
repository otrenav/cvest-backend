
from abc import ABCMeta, abstractmethod

# TODO: Update with latest MongoDatabase


class Database(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, host, port):
        pass

    @abstractmethod
    def read_user(self, email):
        pass

    @abstractmethod
    def read_user_wallets(self, email, wallet_class):
        pass

    @abstractmethod
    def read_user_accounts(self, email, account_class):
        pass

    @abstractmethod
    def _read_user_container(self, email, container):
        pass

    @abstractmethod
    def write_markets(self, exchange, data):
        pass

    @abstractmethod
    def write_assets(self, data):
        pass
