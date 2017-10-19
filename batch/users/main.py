
# FIX BEGIN
# Python 3 imports fix
import sys
sys.path.append("../../")
# FIX END

import logging

from datetime import datetime

from users import User
from scheduler import Scheduler
from databases import MongoDatabase

logging.getLogger().setLevel(logging.WARNING)

USERS = [
    User("otrenav@gmail.com", MongoDatabase()),
    User("rjtr30@gmail.com", MongoDatabase()),
    User("yuli.godinez@gmail.com", MongoDatabase()),
    User("ricargom2000@hotmail.com", MongoDatabase()),
    User("nestor.sag@gmail.com", MongoDatabase()),
    User("rod.cristina28@gmail.com", MongoDatabase()),
    User("ja.morales.alfaro@gmail.com", MongoDatabase())
]


def collect():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
    print("  [+] {}".format(timestamp))
    for user in USERS:
        print("    [+] {} ".format(user.name))
        user.update_assets(timestamp)
    print("  [+] DONE")


def main():
    print("[+] COLLECTING USERS DATA...")
    scheduler = Scheduler().get_scheduler()
    scheduler.add_job(collect, "cron", hour="*")
    # scheduler.add_job(collect, "cron", minute="*/1")
    scheduler.start()


if __name__ == "__main__":
    main()
