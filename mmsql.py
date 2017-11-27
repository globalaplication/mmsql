# -*- coding: utf-8 -*-
#!/usr/bin/env python3

def execute(beta, *VALUES):
    global table, database 
    command = beta.replace('(', ' ( ').replace(')', ' ) ').replace('ROWS',' ROWS ').replace(',', '  ')
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
            if len(database) is 0:
                end = 'end:info:table'
            else: 
                end = ''
            createnewrows = string+':rows:'+ strnewrows+'\n'
            createnewtypes = string+':types:'+strnewtype+'\n'+string+':count:0'+'\n'+database
            database = createnewrows+createnewtypes+end
            update()
        else:
            print('tablo kayıtlı')
    if (command[0:2] == ['INSERT', 'INTO']):
        table = command[2]
        database_get_count = getTableCount(table)
        array_table_rows = []
        for f_table_rows in command[command.index('ROWS')+1:]:
            if (f_table_rows == '(' or f_table_rows == ')'):
                continue
            array_table_rows.append(f_table_rows)
        for for_update in array_table_rows:
            if len(array_table_rows) is len(VALUES):
                database = database + '\n' + 'table:mmsql:' +for_update + ':' + str(database_get_count+1) +'\n'+ VALUES[array_table_rows.index(for_update)] + '\nend'
            else:
                print('hatali kullanim')
                break
        if len(array_table_rows) is len(VALUES):
            database = database.replace('table:'+table+':count:' + str(database_get_count), 'table:'+table+':count:' + str(database_get_count+1))
            update()
        
def update():
    db = open(n, 'w')
    db.write(database)
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
    if len(database) is not 0:
       getTableInfo = database.split('\n')[0:database.split('\n').index('end:info:table')]

connect('database.mmsql')
#execute('CREATE TABLE database (isim:Text soyadi:Text)')
execute('INSERT INTO database ROWS(isim,soyadi)', 'python', 'soyadi')


#print(getRows('deneme'))
#print(getTypes('deneme'))
#print(getTableCount('deneme'))
