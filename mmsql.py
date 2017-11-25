# -*- coding: utf-8 -*-
#!/usr/bin/env python3

def execute(beta):
    global table, database 
    command = beta.replace('(', ' ( ').replace(')', ' ) ')
    command = command.split()
    if (command[0:2] == ['CREATE', 'TABLE']):
        table = command[2]
        string, strnewrows, strnewtype  = ('table:'+table, '', '')
        if database.find(string+':') is -1:
            for frowtype in command:
                if (frowtype is '('):
                    newrowtype = command[command.index(frowtype)+1:-1]
            for fnewrows in newrowtype[0].split(':'):
                strnewrows = strnewrows + fnewrows + ' '
            for fnewtypes in newrowtype[1].split(':'):
                strnewtype = strnewtype + fnewtypes + ' '
            createnewrows = string+':rows:'+ strnewrows+'\n'
            createnewtypes = string+':types:'+strnewtype+'\n'+string+':count:0'+'\n'+database
            database = createnewrows+createnewtypes 
            update()
        else:
            print('tablo kayıtlı')
def update():
    db = open(n, 'w')
    if len(database) is not 0:
        db.write(database)
    else:
    	db.write('table:mmsql:rows:id\n'+'table:mmsql:types:ID\n'+'table:mmsql:count:0\n'+'end:info:table')
    db.close()
def getTableCount(table):
    table = str(table)
    string = 'table:'+table
    count = [count for count in getTableInfo if count.startswith(string+':count:') is True]
    if len(count) is not 0:
        return int(count[-1][len(string+':count:'):].split()[-1])
def getRows(table):
    table = str(table)
    string = 'table:'+table
    Rows = [Rows for Rows in getTableInfo if Rows.startswith(string+':rows:') is True]
    if len(Rows) is not 0:
        return str(Rows[-1][len(string+':rows:'):].split()) #-1:0
def getTypes(table):
    table = str(table)
    string = 'table:'+table
    type = [type for type in getTableInfo if type.startswith(string+':types:') is True]
    if len(type) is not 0:
        return str(type[-1][len(string+':types:'):].split())
def connect(beta):
    import os
    global getTableInfo
    global database, n
    n = beta
    database = ''
    if os.path.lexists(beta) is True:
        file = open(beta)
        database = file.read()
        file.close()
        getTableInfo = database.split('\n')[0:database.split('\n').index('end:info:table')]
        return database
    else:
        update()
    	return -1

connect('database.mmsql')
execute('CREATE TABLE database (isim:Text soyadi:Text)')

#print(getRows('deneme'))
#print(getTypes('deneme'))
#print(getTableCount('deneme'))
