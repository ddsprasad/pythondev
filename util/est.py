def Dict2Str(dictin,joiner=','):
    # make dict to str, with the format key='value'
    #tmpstr=''
    tmplist=[]
    for k,v in dictin.items():
        # if v is list, so, generate
        # "k in (v[0], v[1], ...)"
        if isinstance(v, (list, tuple)):
            tmp = str(k)+' in ('+ ','.join(map(lambda x:'\''+str(x)+'\'',v)) +') '
        else:
            tmp = str(k)+'='+'\''+str(v)+'\''
        tmplist.append(' '+tmp+' ')
    return joiner.join(tmplist)

conf = {'type': 'column',
        'tableName': 'products',
        'columns': ['ProductId INT', 'Color VARCHAR(10)', 'Price INT', 'dt DATETIME' ],
        'key': ['Price','Color'],
        'primarykey': 'ProductId',
        'sharedkey': ['ProductId']}

def list_string(li,type=True):
    if type:
        return "\n,".join(str(x) for x in li)
    else:
        return ",".join(str(x) for x in li)
# print(list_string(['ProductId INT', 'Color VARCHAR(10)', 'Price INT', 'dt DATETIME' ]))

def gen_table_ddl(dictin):
    sql = ''
    if dictin['type'] == 'row':
        sql += 'CREATE TABLE RS_%s ( '%dictin["tableName"].upper()
        sql += '%s ' % list_string(dictin["columns"])
        if isinstance(dictin['key'], list):
            for i in dictin['key']:
                sql += '\n,KEY (%s)' % i
        else:
            sql += '\n,KEY (%s)' % dictin["key"]
        sql += '\n,PRIMARY KEY(%s),' % dictin["primarykey"]
    else:
        sql += 'CREATE TABLE CS_%s ( ' % dictin["tableName"].upper()
        sql += '%s ' % list_string(dictin["columns"])
        if isinstance(dictin['key'], list):
                sql += '\n,KEY (%s) USING CLUSTERED COLUMNSTORE' % list_string(dictin["key"],False)
        else:
            sql += '\n,KEY (%s) USING CLUSTERED COLUMNSTORE' % dictin["key"]


    if isinstance(dictin['sharedkey'], list):
        for i in dictin['sharedkey']:
            sql += '\n,SHARD KEY (%s)'%i
    else:
        sql += '\n,SHARD KEY (%s)'%dictin["key"]
    sql += '\n);'
    return sql

# print(gen_table_ddl(conf))
conf = {'type': 'column',
        'tableName': 'products',
        'columns': ['ProductId INT', 'Color VARCHAR(10)', 'Price INT', 'dt DATETIME' ],
        'key': ['Price','Color'],
        'primarykey': 'ProductId',
        'sharedkey': ['ProductId']}


import json
with open("/home/prasad/PycharmProjects/PythonDev/querybuilder.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)
# print(gen_table_ddl('products',{'columns':['ProductId INT', 'Color VARCHAR(10)', 'Price INT', 'dt DATETIME' ]}))


def gen_update(table,dicts,conddicts):
    # conddicts maybe the Condition, in sql, where key='value' or key in (value)
    # dicts are the values to update
    sql = ''
    sql += 'update %s '%table
    sql += ' set %s'%Dict2Str(dicts)
    sql += ' where %s'%Dict2Str(conddicts,'and')
    return sql

def gen_select(table,keys="*",conddicts=None):
    if isinstance(keys, (tuple,list)):
        keys=','.join(map(str,keys))
    sql = 'select %s '%keys
    sql += ' from %s '%table
    if conddicts:
        sql += ' where %s '%Dict2Str(conddicts,'and')
    #print sql
    return sql

#
# print(Dict2Str(conf))


