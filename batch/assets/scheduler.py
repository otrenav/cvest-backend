
import logging

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

logging.getLogger().setLevel(logging.WARNING)


class Scheduler:

    JOB_DEFAULTS = {'coalesce': True, 'max_instances': 4}
    EXECUTORS = {'default': ThreadPoolExecutor(30)}


    def __init__(self):
        # TODO: Use MongoDB
        jobs_database = 'sqlite:///jobs.sqlite'
        self.JOB_STORES = {'default': SQLAlchemyJobStore(url=jobs_database)}

    def get_scheduler(self):
        return BlockingScheduler(
            jobstores=self.JOB_STORES,
            executors=self.EXECUTORS,
            job_defaults=self.JOB_DEFAULTS
        )
