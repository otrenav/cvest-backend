
from datetime import datetime, timedelta


class TimeProcessor:

    @staticmethod
    def subtract_time(timestamp, interval):
        date_time = datetime.strptime(timestamp, "%Y-%m-%d-%H-%M")
        if interval == '5m':
            date_time -= timedelta(minutes=5)
        elif interval == '1h':
            date_time -= timedelta(hours=1)
        elif interval == '1d':
            date_time -= timedelta(days=1)
        elif interval == '1w':
            date_time -= timedelta(weeks=1)
        elif interval == '1m':
            date_time -= timedelta(weeks=4)
        elif interval == '1y':
            date_time -= timedelta(weeks=52)
        return date_time.strftime("%Y-%m-%d-%H-%M")
