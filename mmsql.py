# -*- coding: utf-8 -*-
#!/usr/bin/env python3


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
    type = [type for type in getTableInfo if type.startswith(string+':type:') is True]
    if len(type) is not 0:
        return str(type[-1][len(string+':type:'):].split())
def connect(beta):
    import os
    global getTableInfo
    global database, n
    n = beta
    if os.path.lexists(beta) is True:
        file = open(beta)
        database = file.read()
        file.close()
        getTableInfo = database.split('\n')[0:database.split('\n').index('end:info:table')]
        return database
    else:
    	return -1
def execute(beta):
    global table, rowtype
    command = beta.replace('(', ' ( ').replace(')', ' ) ')
    command = command.split()
    
    if (command[0:2] == ['CREATE', 'TABLE']):
        table = command[2]
    string = 'table:'+table
    ssetrows = ''
    for frowtype in command:
        if (frowtype is '('):
            rowtype = command[command.index(frowtype)+1:-1]
    
    setrows = rowtype[0].split(':')
    for fsetrows in setrows:
    	ssetrows = ssetrows + fsetrows + ' '
    setdatabase =  'table:' + table + ':rows:' + ssetrows + '\n' + database

    print(setdatabase)


connect('database.mmsql')
execute('CREATE TABLE database (isim:Text soyadi:Text)')

#print(getRows('deneme'))
#print(getTypes('deneme'))
#print(getTableCount('deneme'))
