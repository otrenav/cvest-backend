
from pymongo import MongoClient
from bson.objectid import ObjectId

from utilities.exceptions import CVESTInternalError, CVESTExternalError

from .database import Database
from .mongo_etl import MongoETL
from .constants import USERS, PERSONAL, WALLETS, ACCOUNTS, ASSETS, EXCHANGES

#
# TODO: Extract separate conceptual classes
#


class MongoDatabase(Database):

    def __init__(self, host='localhost', port=27017):
        self.db = MongoClient(host, port)
        self.etl = MongoETL()

    def read_user(self, key, value):
        value = ObjectId(value) if key == "_id" else value
        user = self.db[USERS][PERSONAL].find_one({key: value})
        if user is None:
            msg = "Non-existent user"
            data = {"Key": key, "Value": value}
            raise CVESTInternalError(msg, data)
        return user

    def read_user_assets_time_series(self, user_id):
        #
        # TODO: Add indexes to speed process
        #
        assets = list(self.db[USERS][ASSETS].find({'user_id': user_id}))
        timestamps = sorted(set([asset['timestamp'] for asset in assets]))
        symbols = list(set([asset['symbol'] for asset in assets]))
        markets = list(self.db[EXCHANGES]['coinmarketcap'].find({
            'timestamp': {'$in': timestamps},
            'symbol': {'$in': symbols}
        }))
        return self.etl.assets_time_series(
            assets, markets, symbols, timestamps)

    def read_user_assets_current_status(self, user_id):
        time_series = self.read_user_assets_time_series(user_id)
        return self.etl.assets_current_status(time_series)

    def read_user_assets_balances(self, user_id):
        time_series = self.read_user_assets_time_series(user_id)
        return self.etl.assets_balance(time_series)

    def read_user_wallets(self, email, wallet_class):
        data = self._read_user_container(email, WALLETS)
        return [wallet_class(wallet) for wallet in data]

    def read_user_accounts(self, email, account_class):
        data = self._read_user_container(email, ACCOUNTS)
        return [account_class(account) for account in data]

    def _read_user_container(self, email, container):
        user_id = self.db[USERS][PERSONAL].find_one({"email": email})["_id"]
        return self.db[USERS][container].find({"user_id": user_id})

    def write_user(self, email):
        if self.db[USERS][PERSONAL].find({"email": email}).count() > 0:
            data = {"Email": email}
            msg = "User already exists"
            raise CVESTExternalError(msg, data)
        self.db[USERS][PERSONAL].insert_one({"email": email})

    def write_wallet(self, user_id, symbol, address, note):
        query = {"user_id": user_id, "address": address}
        if self.db[USERS][WALLETS].find(query).count() > 0:
            data = {
                "Email": self._read_user_email(user_id),
                "Address": address
            }
            msg = "Wallet already exists"
            raise CVESTExternalError(msg, data)
        self.db[USERS][WALLETS].insert_one({
            "address": address,
            "user_id": user_id,
            "symbol": symbol,
            "note": note
        })

    def write_account(self, user_id, exchange, key, secret):
        query = {"user_id": user_id, "exchange": self._slugify(exchange)}
        if self.db[USERS][ACCOUNTS].find(query).count() > 0:
            msg = "Account already exists"
            data = {
                "Email": self._read_user_email(user_id),
                "Exchange": exchange,
                "Key": key
            }
            raise CVESTExternalError(msg, data)
        self.db[USERS][ACCOUNTS].insert_one({
            "exchange": self._slugify(exchange),
            "user_id": user_id,
            "secret": secret,
            "key": key
        })

    def write_markets(self, exchange, data):
        exchange = self._slugify(exchange)
        self.db[EXCHANGES][exchange].insert_many(data)

    def write_assets(self, data):
        if len(data) > 0:
            self.db[USERS][ASSETS].insert_many(data)

    def update_user_name(self, email, name):
        self.db[USERS][PERSONAL].update(
            {"email": email},
            {"$set": {"name": name}}
        )

    def _read_user_email(self, user_id):
        return self.db[USERS][PERSONAL].find_one({"_id": user_id})["email"]

    def _slugify(self, string):
        return string.lower().replace(" ", "-")
