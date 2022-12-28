from datetime import datetime, time

from pydantic import BaseModel


class InstructionData(BaseModel):
    user_id: int
    key_text: str
    message_id: int


class NotificationData(BaseModel):
    user_id: int
    notif_text: str
    exec_datetime: datetime


class RemindsData(BaseModel):
    user_id: int
    rem_text: str
    exec_time: time
    day_cycle: int
