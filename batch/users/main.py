
# FIX BEGIN
# Python 3 imports fix
import sys
sys.path.append("../../")
# FIX END

import datetime

from pprint import pprint

from users import User
from scheduler import Scheduler


USERS = [
    User('otrenav@gmail.com'),
    User('rjtr30@gmail.com'),
    User('yuli.godinez@gmail.com'),
    # User('yuli.godinez@gmail.com'),
    # User('yuli.godinez@gmail.com'),
    # User('yuli.godinez@gmail.com')
]


def collect():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d, %H:%M")
    print("  [+] COLLECTING: " + date_time + " ... ", end="")
    for user in USERS:
        assets = user.update_assets()
        pprint(assets)
    print("DONE")


def main():
    print("[+] COLLECTING PORTFOLIO DATA...")
    scheduler = Scheduler().get_scheduler()
    scheduler.add_job(collect, "cron", minute="*/5")
    # scheduler.add_job(collect, "cron", minute="*/1")
    scheduler.start()


if __name__ == "__main__":
    main()
