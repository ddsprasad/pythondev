from memsql.common import database
import sys
from datetime import datetime


DATABASE = 'PREPDB'
HOST = '10.1.100.12'
PORT = '3306'
USER = 'root'
PASSWORD = 'In5pir0n@121'

def get_connection(db=DATABASE):
    """ Returns a new connection to the database. """
    return database.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=db)

def run_temp_scheduler():
    with get_connection() as conn:
        x = conn.query("call tvf_temp_scheduler()")
        for i in x:
            if 'ERROR' in str(list(i.values())):
                print(datetime.now(), ': ', list(i.values()))
                sys.exit()
            else:
                print(datetime.now(), ': ', list(i.values()))
                print(datetime.now(), ": TEMP TABLES PERSISTED SUCCESSFULLY")


run_temp_scheduler()