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

    global table, database

    if (command[0:2] == ['CREATE', 'TABLE']):

        table, string, strnewrows, strnewtypes  = (command[2], 'table:' + command[2], '', '')

        if database.find(string+':') is -1:

            for frowstypes in command:
                if (frowstypes is '('):
                    newrowstypes = command[command.index(frowstypes)+1:-1]
            for fnewrows in newrowstypes[0].split(':'):
                strnewrows = strnewrows + fnewrows + ' '
            for fnewtypes in newrowstypes[1].split(':'):
                strnewtypes = strnewtypes + fnewtypes + ' '
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

    if (command[0:2] == ['INSERT', 'INTO']):

        database_get_count, table, array_table_rows = TableGetCount(command[2]), command[2], []

        for f_table_rows in command[command.index('ROWS')+1:]:
            if (f_table_rows == '(' or f_table_rows == ')'):
                continue
            if (f_table_rows == 'NOT'): 
                break
            array_table_rows.append(f_table_rows)
            
        print(array_table_rows)

        for for_update in array_table_rows:
            if len(array_table_rows) is len(VALUES):
                database = database + '\n' +'table:'+table+':'+for_update+':'+str(database_get_count+1)+'\n'+VALUES[array_table_rows.index(for_update)]+'\nend'
            else:
                print('hatali kullanim')
                break
        if len(array_table_rows) is len(VALUES):
            database = database.replace('table:'+table+':count:'+str(database_get_count),'table:'+table+':count:'+str(database_get_count+1))
            update()


def update():
    global n
    db = open(n, 'w')
    db.write(database)
    db.close()

def TableGetCount(table):
    
    global getAllTable

    table = str(table)

    string = ('table:'+table)

    count = [count for count in getAllTable if count.startswith(string+':count:')]

    if len(count) is not 0:
        
        return int(count[-1][len(string+':count:'):].split()[-1])

def TableGetRows(table):

    global getAllTable

    table = str(table)

    string = ('table:'+table)

    Rows = [Rows for Rows in getAllTable if Rows.startswith(string+':rows:')]

    if len(Rows) is not 0:

        return str(Rows[-1][len(string+':rows:'):].split()) #-1:0

def TableGetTypes(table):

    global getAllTable

    table = str(table)

    string = ('table:'+table)

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

connect('database.mmsql')
execute('CREATE TABLE  mmsql (isim:Text soyadi:Text)')
#print(getAllTable)
execute('INSERT INTO database ROWS(isim,soyadi) NOT(isim)', 'python', 'soyadi')


#print(getRows('deneme'))
#print(getTypes('deneme'))
#print(TableGetCount('mmsql'))
