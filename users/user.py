
from utilities.exceptions import ExternalError

from assets.wallets import Wallet
from assets.accounts import Account


class User:

    name = ''

    def __init__(self, email=None, db=None, new=False, user_id=None):
        self.db = db
        if user_id:
            self._read_user("_id", user_id)
        elif not new:
            self._read_user("email", email)
        else:
            self._new_user(email)

    def update_name(self, name):
        self.db.update_user_name(self.email, name)
        self.name = name
        return self

    def update_assets(self, timestamp):
        assets = []
        for wallet in self._wallets():
            try:
                assets += wallet.update_assets(timestamp, self.db)
            except ExternalError:
                pass
        for account in self._accounts():
            try:
                assets += account.update_assets(timestamp, self.db)
            except ExternalError:
                pass
        return assets

    def assets_time_series(self):
        return self.db.read_user_assets_time_series(self.user_id)

    def new_wallet(self, symbol, address, note=""):
        self.db.write_wallet(self.user_id, symbol, address, note)

    def new_account(self, exchange, key, secret):
        self.db.write_account(self.user_id, exchange, key, secret)

    def _read_user(self, key, value):
        user = self.db.read_user(key, value)
        self.name = user.get("name")
        self.email = user["email"]
        self.user_id = user["_id"]

    def _new_user(self, email):
        self.db.write_user(email)
        self._read_user("email", email)

    def _wallets(self):
        return self.db.read_user_wallets(self.email, Wallet)

    def _accounts(self):
        return self.db.read_user_accounts(self.email, Account)
