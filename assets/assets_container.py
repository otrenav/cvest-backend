

class AssetsContainer:

    user_id = None

    def update_assets(self, timestamp, db):
        """Update assets by getting the latest data from the wallet inside the
        blockchain and saving it to the database with a new timestamp. This
        function should only be used by batch processes. It should not be used
        by any of the front ends.
        """
        print("      [+] {}".format(self.container))
        self.timestamp = timestamp
        assets = self.assets()
        db.write_assets(self._dicts(assets))
        return assets

    def assets(self):
        return self._insert_metadata(self._get_assets())

    def _insert_metadata(self, assets):
        for asset in assets:
            asset.set_timestamp(self.timestamp)
            asset.set_user_id(self.user_id)
        return assets

    def _dicts(self, assets):
        return [asset.__dict__ for asset in assets]
