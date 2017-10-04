
from pprint import pprint

from pymongo import MongoClient

from .database import Database
from .constants import USERS, PERSONAL, EXCHANGES, ASSETS


class MongoDatabase(Database):

    def __init__(self, host='localhost', port=27017):
        self.mongo_client = MongoClient(host, port)

    def read_user(self, email):
        collection = self.mongo_client[USERS][PERSONAL]
        user = collection.find({"email": email})
        pprint(user)
        return user

    def write_assets(self, exchange, assets):
        collection = self.mongo_client[EXCHANGES][exchange]
        self.collection.insert_many(assets)
