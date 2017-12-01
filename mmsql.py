# -*- coding: utf-8 -*-
#!/usr/bin/env python3
def execute(beta, *VALUES):
    REpL = {'(':' ( ', ')':' ) ', 
        'ROWS':' ROWS ', 
        ',':'  ', '*':' * '}
    for keys in REpL.keys():
        beta = beta.replace(keys, REpL[keys])
    command = beta.split()
    NOT, PNOT, TFNOT, ROWS, PROWS, SORT, PSORT = [], [], [], [], [], [], []
    global table
    global database
    if 'NOT' in command:
        if (command[command.index('NOT')+1] == '('):
            for FNOT in command[command.index('NOT')+1:]:
                if FNOT is '(': continue
                if FNOT is ')': break
                PNOT.append(FNOT)
            NOT.extend(PNOT)
    if 'ROWS' in command:
        if (command[command.index('ROWS')+1] == '('):
            for FROWS in command[command.index('ROWS')+1:]:
                if FROWS is '(': continue
                if FROWS is ')': break
                PROWS.append(FROWS)
            ROWS.extend(PROWS)
    if 'SORT' in command:
        if (command[command.index('SORT')+1] == '('):
            for FSORT in command[command.index('SORT')+1:]:
                if FSORT is '(': continue
                if FSORT is ')': break
                PSORT.append(FSORT)
            SORT.extend(PSORT)
    if (command[0:2] == ['INSERT', 'INTO']):
        table = command[2]
    if (command[0:3] == ['SELECT', '*', 'FROM']):
        table = command[3]
    if (command[0:2] == ['CREATE', 'TABLE']):
        table = command[2]
    if (command[0:2] == ['CREATE', 'TABLE']):
        string, strnewrows, strnewtypes  = ('table:' + table, '', '')
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
            createnewrows = string+':rows:' + strnewrows+'\n'
            createnewtypes = string+':types:'+ strnewtypes+'\n'+string+':count:0'+'\n'+database
            database = createnewrows + createnewtypes + end 
            update()
        else:
            print(table, 'tablo kayitli')
    if (command[0:2] == ['INSERT', 'INTO']):
        DatabaseGetCount = TableGetCount(table)
        for insert in ROWS:
            if len(ROWS) is len(VALUES):
                start1  = 'table:' + table + ':' + insert + ':' + str(DatabaseGetCount+1)
                end1 = VALUES[ROWS.index(insert)] + '\nend'
                database = database + '\n' + start1 +'\n'+ end1
            else:
                print('hatali kullanim')
                break
        if len(ROWS) is len(VALUES):
            start = 'table:' + table +':count:' + str(DatabaseGetCount)
            end = 'table:' + table +':count:' + str(DatabaseGetCount+1)
            database = database.replace(start, end)
            if len(NOT) > 0 and NOT[0] not in ROWS:
                print('hatali kullanim', NOT, ROWS)
            else:
                for id in range(1, TableGetCount(table)+1):
                    if len(NOT) > 0 and VALUES[ROWS.index(NOT[0])] == GetColumn(table, id)[1:][ROWS.index(NOT[0])]:
                        TFNOT.append(1)
        if (len(TFNOT) is 0):
            update()
        else:
            print('kayitli!')
    if (command[0:3] == ['SELECT', '*', 'FROM']):
        connect(n)
        if len(VALUES) is not 0:
            start, end, tgcount = VALUES[0], VALUES[1], TableGetCount(table)
        if len(VALUES) is 0:
            start, end = 1, TableGetCount(table)
        if len(SORT) is 0:
            select = [GetColumn(table, select) for select in range(start, end+1) if (select < tgcount+1)]
            return select
        elif SORT[0] == 'ZA':
            select = [GetColumn(table, select) for select in range(end, start-1, -1) if (select <= tgcount)]
            return select
        elif SORT[0] == 'AZ':
            select = [GetColumn(table, select) for select in range(start, end+1) if (select < tgcount+1)]
            return select
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
    if len(count) is 0:
        return 0
def TableGetRows(table):
    global getAllTable
    string = ('table:'+str(table))
    Rows = [Rows for Rows in getAllTable if Rows.startswith(string+':rows:')]
    if len(Rows) is not 0:
        return Rows[0][len(string+':rows:'):].split()
    if len(Rows) is 0:
        return 0
def TableGetTypes(table):
    global getAllTable
    string = ('table:'+str(table))
    type = [type for type in getAllTable if type.startswith(string+':types:')]
    if len(type) is not 0:
        return str(type[-1][len(string+':types:'):].split())
def DELETE_ID_(table, id):
    global database
    id, table = str(id), str(table)
    if database.find(table+':'+'id'+':'+id+':hide') is -1:
        database = database + '\n' + table+':'+'id'+':'+id+':hide'
        update()
def connect(beta):
    import os
    global getAllTable, database, n
    database, n = ('', beta)
    if os.path.lexists(beta) is False:
        with open(beta, 'w') as file:
            file.write('table:beta:rows:test\ntable:beta:types:Text\ntable:beta:count:0\nend:info:table')
    file = open(beta)
    database = file.read()
    file.close()
    getAllTable = database.split('\n')[0:database.split('\n').index('end:info:table')]
def GetColumn(table, id):
    global database
    table, id, gets = str(table), str(id), []
    for test in TableGetRows(table):
        output = []
        search = 'table'+':'+table+':'+test+':'+id+'\n'
        start = database.find(search)
        end = database.find('\nend', start+len(search))
        output = [database[start+len(search):end]]
        if start is not -1 and database.find(table+':'+'id'+':'+id+':hide') is -1: 
            gets.extend(output)
        if start is not -1 and database.find(table+':'+'id'+':'+id+':hide') is not -1: 
            gets.extend(['Null'])
    gets.insert(0, int(id))
    return gets
connect('database.mmsql')
execute('CREATE TABLE  mmsql ( isim:Text soyadi:Text )')
execute('INSERT INTO mmsql ROWS ( isim, soyadi ) NOT (isim)',  'python', 'programlama')
#update()
for test in execute('SELECT * FROM mmsql SORT (ZA)', 1, 50):
    print(test)
#DELETE_ID_('mmsql', 1)
#print(GetColumn('mmsql', 1))
