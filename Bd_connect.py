import psycopg2
from constants import *
import pydantic

conn = psycopg2.connect(host="localhost",
    database=KEYS.db_name,
    user=KEYS.db_login,
    password=KEYS.db_pass)

class DataBase():
    conn = None
    cursor = None 

    def __init__(self) -> None:
        self.conn = psycopg2.connect(host="localhost",
        database=KEYS.db_name,
        user=KEYS.db_login,
        password=KEYS.db_pass)
        
        self.cursor = self.conn.cursor()
    
    

