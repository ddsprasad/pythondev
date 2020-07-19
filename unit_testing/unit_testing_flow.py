import mysql.connector
import json


config = {
  'user': 'root',
  'password': 'In5pir0n@121',
  'host': '10.1.100.12',
  'database': 'PREPDB',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

# con = mysql.connector.connect(
#     user = 'ardit700_student',
#     password= 'ardit700_student',
#     host = '108.167.140.122',
#     database = 'ardit700_pm1database'
# )
with open("/home/prasad/PycharmProjects/PythonDev/unit_testing/testdata.txt", "r") as read_file:
    # conf = json.load(read_file)
    conf = str(read_file.readlines()).replace('[','').replace(']','')

print(conf)
print(type(conf))
#print(cnx)

cusr = cnx.cursor()
# #
print("Initiate the Process")
# step1_qry = "call sp_load_ut_metadata(%s)"
conf = str({"metric_name":"sales_revenue_fact",
"qclass_group":"basic",
"metric_function":"default",
"question":"Show me  sales revenue by region in November 2019 for TMC & ACCESSORIES",
"table_qry":"SELECT TIME AS `Time`,RGN_DESC AS `Region`,VSB_EMO_SPCE AS `Emotional Space`,SUM(SALES_SUM) AS `SALES Revenue` FROM PREPDB.CS_DP_VSB_SALES_CUBOID_TESTING456 WHERE CUBOIDID = ''WPSCTABCDSFOGHIJKLMNEQRTUVWXDRCAEDPV'' AND TIME IN (201910) AND VSB_EMO_SPCE IN (''TMC'',''ACCESSORIES'') GROUP BY RGN_DESC, VSB_EMO_SPCE  ORDER BY `SALES Revenue` DESC;",
"tvf_parameters": [
  "sales_revenue",
  "WPSCTABCDSFOGHIJKLMNEQRTUVWXDRCAEDPV",
  "RGN_DESC AS `Region`,VSB_EMO_SPCE AS `Emotional Space`",
  "`SALES Revenue`",
  "SUM(SALES_SUM)",
  "WEEK",
  "IN (201910)",
  "VSB_EMO_SPCE IN (''TMC'',''ACCESSORIES'')",
  "RGN_DESC, VSB_EMO_SPCE",
  "",
  "`SALES Revenue` DESC",
  ""
        ]})

result_args = cusr.callproc('sp_load_ut_metadata',[conf,0])
print(result_args[1])
# cusr.execute(f"call sp_load_ut_metadata({conf})")
case_id = cusr.execute("SELECT case_id FROM cs_ut_metadata_tbl order by ins_ts desc limit 1")
print(f"Registered Test Metadata, CASE_ID genrated: {case_id}")

# step2_qry = "call sp_ut_kmm_tvf(%s)"
# step2_values = (case_id)
# cusr.execute(step2_qry,step2_values)
# print(f"Tested CASE_ID: {case_id}")




#
# resutls = cusr.fetchall()
#
# for i in resutls:
#     print("-----------\n")
#     print(i[2])




cnx.close()
