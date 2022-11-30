from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, Time
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import ValidationError

from constants import *


Base = declarative_base()
engine = create_engine(f'postgresql+psycopg2://{KEYS.db_login}:{KEYS.db_pass}@localhost:5432/{KEYS.db_name}',\
        echo=False, future=True)


class Instruction(Base):
    __tablename__ = 'instructions'


    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    key_text = Column(String)
    message_id = Column(Integer)

    def __repr__(self) -> str:
        return f'Instruction(id={self.id!r}, user_id={self.user_id!r}, key_text={self.key_text!r}, message_id={self.message_id!r})'
    
    # def create_table(self):
    #     Base.metadata.create_all(engine)


class Notification(Base):
    __tablename__ = 'notifications'


    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    notif_text = Column(String)
    exec_datetime = Column(DateTime)

    def __repr__(self) -> str:
        return f'Instruction(id={self.id!r}, user_id={self.user_id!r}, notif_text={self.notif_text!r}, exec_datetime={self.exec_datetime!r})'

    # def create_table(self):
    #     Base.metadata.create_all(engine)


