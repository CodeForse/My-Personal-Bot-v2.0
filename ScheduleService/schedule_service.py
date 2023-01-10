import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from DataBase.crud_service import *
from ScheduleService.jobs import send_message_remind


class Schedule:
    def __init__(self, db: Session):
        self.scheduler = BlockingScheduler()
        reminds = get_reminds_all(db)
        for remind in reminds:
            trigger = CronTrigger(hour=remind.exec_time.hour, minute=remind.exec_time.minute)
            args = (remind.user_id, remind.rem_text)
            self.scheduler.add_job(send_message_remind, trigger, args=args, id=str(remind.id), days=remind.day_cycle,
                                   start_date=remind.next_execute_day)

    def delete_job_by_id(self, db: Session, user_id, id):
        del_remind(db, user_id, id)
        self.scheduler.remove_job(id)

    def add_job(self, db: Session, user_id, id, rem_text: str, exec_time: time, day_cycle: int):
        id = add_remind(db, user_id, rem_text, exec_time, day_cycle)

        trigger = CronTrigger(hour=exec_time.hour, minute=exec_time.minute)
        args = (user_id, rem_text)
        self.scheduler.add_job(send_message_remind, trigger, args=args, id=str(id), days=day_cycle,
                               start_date=datetime.today())
    

with Session(engine) as db:
    Schedule(db)
