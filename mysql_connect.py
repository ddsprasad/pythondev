import mysql.connector


config = {
  'user': 'lbdev01',
  'password': 'V$B_&*(',
  'host': '10.1.100.12',
  'database': 'PREPDB',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cusr = cnx.cursor()

query = cusr.execute("CALL PREPDB.p2_test(1)")
# query1 = cusr.execute("CALL PREPDB.p2(1)")

# print((query))
# print(type(query1))

resutls = cusr.fetchall()

for i in resutls:
    print("-----------\n")
    print((i))