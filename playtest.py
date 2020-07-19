import json

# conf = {"type":"row",
# "tableName":"products",
# "sharedkey":["ProductId"],
# "primarykey":"ProductId",
# "prefix":"STG",
# "key":["Price","Color"],
# "columns":[
#   {"name":"ProductId","datatype":"INT","isNullable":"False","defalut":"NULL"},
#   {"name":"Color","datatype":"VARCHAR","isNullable":"False","defalut":"NULL"},
#   {"name":"Price","datatype":"INT","isNullable":"False","defalut":"NULL"},
#   {"name":"Sale_Amount","datatype":"DECIMAL","isNullable":"False","defalut":"NULL"},
#   {"name":"Satus_DT","datatype":"DATETIME","isNullable":"False","defalut":"NULL"}]}

with open("/home/prasad/PycharmProjects/PythonDev/qry_builder_createTable.json", "r") as read_file:
    conf = json.load(read_file)

def get_columns():
    sql = ''
    for i in conf["columns"]:
        if i["datatype"].lower() == 'int':
            sql += "\n,"+"`"+i["name"].upper()+"`"+" "+i["datatype"].lower()+"(11)"+" "+"DEFALUT"+" "+i["defalut"]
        elif i["datatype"].lower() == 'varchar':
            sql += "\n," + i["name"].upper() + " " + i["datatype"].lower() + "(255)"+" "+"CHARACTER SET utf8 COLLATE utf8_general_ci"+" "+ "DEFALUT" + " " +i["defalut"]
        elif i["datatype"].lower() == 'decimal':
            sql +="\n," + i["name"].upper() + " " + i["datatype"].lower() + "(255)" + " " + "DEFALUT" + " " + i["defalut"]
        elif i["datatype"].lower() == 'timestamp' or i["datatype"].lower() == 'datetime' :
            sql +="\n," + i["name"].upper() + " " + i["datatype"].lower() + " " + "DEFALUT" + " " + i["defalut"]
        else:
            "Print Enter some Datatype"
    return sql[2:]

print(get_columns())
