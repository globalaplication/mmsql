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
        source = file.read()
        file.close()
        getTableInfo = source.split('\n')[0:source.split('\n').index('end:info:table')]
        return source
    else:
    	return -1
