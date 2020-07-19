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

def load_metadata(inputjson):
    with get_connection() as conn:
        x = conn.query("call sp_load_ut_metadata(%s)" % inputjson)
        for i in x:
            if 'ERROR' in str(list(i.values())):
                print(datetime.now(), ': ', list(i.values()))
                sys.exit()
            else:
                print(datetime.now(), ': ', list(i.values()))
                #print(datetime.now(), ": TEST META DATA LOADED SUCCESSFULLY")

def get_caseid():
    with get_connection() as conn:
        case_id = conn.get("SELECT case_id FROM cs_ut_metadata_tbl order by ins_ts desc limit 1").case_id
        print(datetime.now(), f": GENERATED CASE_ID {case_id}")

def run_unitest():
    with get_connection() as conn:
        case_id = conn.get("SELECT case_id FROM cs_ut_metadata_tbl order by ins_ts desc limit 1").case_id
        x = conn.query("call sp_ut_kmm_tvf('%s')" % case_id)
        for i in x:
            if 'ERROR' in str(list(i.values())):
                print(datetime.now(), ': ', list(i.values()))
                sys.exit()
        # print(datetime.now(), ': ', list(i.values()))
        print(datetime.now(), ": UNIT TESING DONE SUCCESSFULLY")


def get_case_result():
    with get_connection() as conn:
        result = conn.get(
            "SELECT concat(' ',case_id,' : ',result) as result FROM cs_ut_log_tbl where ins_ts = (select max(ins_ts) from cs_ut_log_tbl)").result
        print(datetime.now(), f': TEST RESULT FOR CASE ID {result}')

#
# def get_temp_log():
#     with get_connection() as conn:
#         case_id = conn.get("SELECT case_id FROM cs_ut_metadata_tbl order by ins_ts desc limit 1").case_id
#         request_id = conn.get("select request_id from  cs_ut_log_tbl where case_id = '%s'" %case_id).request_id
#         result = conn.get(
#             "select concat('','   tvf:',tvf_id,'   temp_tbl:',temp_tbl,'   reqid:',request_id, '   status:',status) as log from rs_tvf_log_tbl where request_id = '%s'" %request_id).log
#         print(datetime.now(), f': TEMP-LOG-DATA ===> {result}')





with open("/home/prasad/PycharmProjects/PythonDev/unit_testing/testing_data_2.txt", "r") as read_file:
    # conf = json.load(read_file)
    conf = read_file.readlines()
    for i in conf:
        load_metadata(i)
        get_caseid()
        run_unitest()
        get_case_result()
        # get_temp_log()
        # run_temp_scheduler()
        print('==='*15)





# get_temp_scheduler()