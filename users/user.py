
from databases import MongoDatabase


class User:

    def __init__(self, email=''):
        self.email = email
        self.name = ''
        self.assets = []
        self.wallets = []
        self.accounts = []
        self.preferences = {}
        self.db = MongoDatabase()
        self._read_user_data()

    def update_assets(self):
        pass

    def _read_user_data(self):
        user = self.db.read_user_data(self.email)
        self.email = user["email"]
        self.name = user["name"]
        self.assets = user["assets"]
        self.wallets = user["wallets"]
        self.accounts = user["accounts"]
        self.preferences = user["preferences"]
