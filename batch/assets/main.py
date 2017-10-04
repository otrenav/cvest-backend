
# FIX BEGIN
# Python 3 imports fix
import sys
sys.path.append('../../')
# FIX END

import datetime

from pprint import pprint

from exchanges import Exchange
from databases import MongoDatabase
from scheduler import Scheduler

DB = MongoDatabase()

EXCHANGES = [Exchange('CoinMarketCap')]


def collect():
    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d, %H:%M')
    print("  [+] COLLECTING: " + date_time + " ... ", end='')
    for exchange in EXCHANGES:
        assets = exchange.update_assets()
        # TODO: Index: MARKET-TIME
        # pprint(assets)
    print("DONE")


def main():
    print("[+] COLLECTING MARKET DATA...")
    scheduler = Scheduler().get_scheduler()
    scheduler.add_job(collect, 'cron', minute='*/5')
    # scheduler.add_job(collect, 'cron', minute='*/1')
    scheduler.start()


if __name__ == '__main__':
    main()
