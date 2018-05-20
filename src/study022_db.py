# -*- coding: utf-8 -*-
import sqlite3

# 获取数据库连接
def get_conn():
    return sqlite3.connect("py_test.db")

# 获取数据库Cursor
def get_cursor(conn):
    return conn.cursor()

# 执行数据库语句
def db_exe(conn,cursor,sql):
    cursor.execute(sql)
    if "select" not in sql:
        conn.commit()

def db_close(cursor,conn):
    cursor.close()
    conn.close()

def createtable():
    conn = sqlite3.connect("py_test.db")
    cursor = conn.cursor()
    cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
    cursor.execute("insert into user(id,name) values ('1','lishaoquan')")
    print("当前数据行数：",cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

def querydata():
    conn = get_conn()
    cursor = get_cursor(conn)
    db_exe(conn,cursor,"select * from user where id = 1")
    values = cursor.fetchall()
    print(values)
    db_close(cursor,conn)

def deletedata():
    conn = get_conn()
    cursor = get_cursor(conn)
    db_exe(conn,cursor,"delete from user where id = 1")
    db_close(cursor, conn)

if __name__ == "__main__":
    querydata()
    deletedata()
    querydata()