from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from constants import *


Base = declarative_base()

class Instruction(Base):
    __tablename__ = 'Instructions'
    engine = create_engine(f'postgresql+psycopg2://{KEYS.db_login}:{KEYS.db_pass}@localhost:5432/{KEYS.db_name}',\
        echo=True, future=True)

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    key_text = Column(String)
    message_id = Column(Integer)

    def __repr__(self) -> str:
        return f'Instruction(id={self.id!r}, user_id={self.user_id!r}, key_text={self.key_text!r}, message_id={self.message_id!r})'
    
    def create_table(self):
        Base.metadata.create_all(self.engine)
    

    
Instruction().create_table()