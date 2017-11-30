# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os

def execute(beta, *VALUES):
    REpL = {'(':' ( ', ')':' ) ', 
        'ROWS':' ROWS ', 
        ',':'  '}
    for keys in REpL.keys():
        beta = beta.replace(keys, REpL[keys])
    command = beta.split()
    global table
    global database
    if (command[0:2] == ['CREATE', 'TABLE']):
        table, string, strnewrows, strnewtypes  = (command[2], 'table:' + command[2], '', '')
        if database.find(string+':') is -1:
            for frowstypes in command:
                if (frowstypes is '('):
                    newrowstypes = command[command.index(frowstypes)+1:-1]
            for index in range(0, len(newrowstypes)):
                strnewrows = strnewrows + newrowstypes[index].split(':')[0] + ' '
                strnewtypes = strnewtypes + newrowstypes[index].split(':')[1] + ' '
            if len(database) is 0:
                end = 'end:info:table'
            elif len(database) > 0:
                end = ''
            createnewrows = string+':rows:'+ strnewrows+'\n'
            createnewtypes = string+':types:'+strnewtypes+'\n'+string+':count:0'+'\n'+database

            database = createnewrows + createnewtypes + end
            update()
        else:
            print(table, 'tablo kayitli')
def update():
    global n
    db = open(n, 'w')
    db.write(database)
    db.close()
def TableGetCount(table):
    global getAllTable
    string =  ('table:'+str(table))
    count = [count for count in getAllTable if count.startswith(string+':count:')]
    if len(count) is not 0:
        return int(count[-1][len(string+':count:'):].split()[-1])
def TableGetRows(table):
    global getAllTable
    string = ('table:'+str(table))
    Rows = [Rows for Rows in getAllTable if Rows.startswith(string+':rows:')]
    if len(Rows) is not 0:
        return Rows[-1][len(string+':rows:'):].split() #-1:0
def TableGetTypes(table):
    global getAllTable
    string = ('table:'+str(table))
    type = [type for type in getAllTable if type.startswith(string+':types:')]
    if len(type) is not 0:
        return str(type[-1][len(string+':types:'):].split())
def connect(beta):
    global getAllTable, database, n
    database, n = ('', beta)
    if os.path.lexists(beta) is True:
        file = open(beta)
        database = file.read()
        file.close()
    if len(database) is not 0:
       getAllTable = database.split('\n')[0:database.split('\n').index('end:info:table')]
def GetColumn(table, id):
    global database
    table, id, gets = str(table), str(id), []
    for test in TableGetRows(table):
        search = 'table'+':'+table+':'+test+':'+id+'\n'
        start = database.find(search)
        end = database.find('\nend', start+len(search))
        output = [database[start+len(search):end]]
        if start is not -1:
            gets.extend(output)
    return gets

connect('database.mmsql')
execute('CREATE TABLE  mmsql ( isim:Text soyadi:Text )')
#print(getAllTable)
execute('INSERT INTO mmsql ROWS(isim,soyadi)  ', 'python', 'programlama')

#print(GetColumn('mmsql', 1))

