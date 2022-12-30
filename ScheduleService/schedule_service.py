from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from DataBase.crud_service import *
from ScheduleService.jobs import send_message_remind


class Schedule:
    def __init__(self, db: Session):
        self.scheduler = BackgroundScheduler()
        reminds = get_reminds_all(db)
        for remind in reminds:
            trigger = CronTrigger(hour=remind.exec_time.hour, minute=remind.exec_time.minute)
            args = (remind.user_id, remind.rem_text)
            self.scheduler.add_job(send_message_remind, trigger, args=args, id=remind.id)

    def delete_job_by_id(self, db: Session, user_id, id):
        self.scheduler.remove_job(id)
        del_remind(db, user_id, id)

    # def add_job(self, db:Session, user_id, id):
