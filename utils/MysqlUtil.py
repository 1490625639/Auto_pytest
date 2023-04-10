# -*- coding:utf-8 -*-

# 1 创建封装类
import pymysql
import pymysql.cursors

from utils.LogUtil import my_log
class Mysql:
    # 2 初始化数据,链接数据库,光标对象
    def __init__(self, host, user, password, database, charset, port):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        # 2 初始化数据,链接数据库,光标对象
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 3 创建询\执行方法
    def fetchone(self, sql):
        """单个查询"""
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        """多个查询"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        try:

            if self.conn and self.cursor:
                self.cursor.execute(sql)
                #             #无论是新增删除还是修改，都要通过事务进行操作
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("执行失败")
            self.log.error(ex)
            return False
        return True

    # 4 关闭数据库
    def _del_(self):
        # 光比光标对象
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    mysql = Mysql("localhost", "root", "123456", "prac", "utf8", 3306)
    #res = mysql.fetchall("select * from a")
    res=mysql.exec()
    print(res)
"""  练习使用
# 1导入pymysql
# 2链接数据库database
# 3获取执行sql的光标对象
# 4执行sql
# 5关闭对象

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="qiyuesuotest",
    charset="utf8",
    port=3306
)

cursor = conn.cursor()

sql = "select * from qiyuesuotest"
cursor.execute(sql)
cursor.fetchone()
"""
