
# FIX BEGIN
# Python 3 imports fix
import sys
sys.path.append("../../")
# FIX END

import logging

from datetime import datetime

from scheduler import Scheduler
from databases import MongoDatabase
from assets.exchanges import Exchange


logging.getLogger().setLevel(logging.WARNING)

EXCHANGES = [
    Exchange("CoinMarketCap", '', ''),
]


def collect():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
    print("  [+] {}".format(timestamp))
    for exchange in EXCHANGES:
        print("    [+] {} ".format(exchange.name))
        exchange.update_markets(timestamp, MongoDatabase())
    print("  [+] DONE")


def main():
    print("[+] COLLECTING EXCHANGES DATA...")
    scheduler = Scheduler().get_scheduler()
    scheduler.add_job(collect, "cron", minute="*/5")
    # scheduler.add_job(collect, "cron", minute="*/1")
    scheduler.start()

if __name__ == "__main__":
    main()
