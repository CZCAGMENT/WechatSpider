# -*- coding: utf-8 -*-
# Author:   BinBin
# Email:    289594665@qq.com
# Time :    2017/07/27

import pyodbc

class DBHelper(object):

    def __init__(self, serverIp, port, dbName, uid, pwd):
        conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s,%s;UID=%s;PWD=%s' % (dbName, serverIp, port, uid, pwd)
        self.connection = pyodbc.connect(conn_info, unicode_results=True)
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            print(self.cursor, '__del__ cursor closed')
        if self.connection:
            self.connection.close()
            self.connection = None

    def destroy(self):
        if self.cursor:
            print(self.cursor, 'destroy cursor closed')
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    # 获取全部查询结果
    def queryAll(self, qryStr):
        print(qryStr.decode('gbk'))
        self.cursor.execute(qryStr)
        return self.cursor.fetchall()

    # 获取前maxcnt条查询结果
    def querySome(self, qryStr, maxCount):
        self.cursor.execute(qryStr)
        return self.cursor.fetchmany(maxCount)

    #获取分页查询结果
    def queryPage(self, qryStr, skipCnt, pageSize):
        self.cursor.execute(qryStr)
        self.cursor.skip(skipCnt)
        return self.cursor.fetchmany(pageSize)

    #获取查询条数
    def count(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    #执行语句，包括增删改，返回变更数据数量
    def execute(self, sql):
        count = self.cursor.execute(sql).rowcount
        self.connection.commit()
        return count

db = DBHelper('120.**.215.***', '1433', 'dbname', 'sa', '*****')