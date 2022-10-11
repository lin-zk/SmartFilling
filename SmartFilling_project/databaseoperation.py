import sqlite3
import time
import os
from datetime import datetime


class Database:
    """为登录界面所提供数据库操作的类"""

    def __init__(self, db, type=0):
        folder=os.path.exists(r'.\database')
        if not folder:
            os.makedirs(r'.\database')
        else:
            pass
        self._database = db
        if type==0:
            self.create_table()
        elif type==1:
            self.create_table(1)

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, db):
        self._database = db

    def create_table(self, type=0):
        """创建一个数据库,如果type=0,创建后台数据库，type=1，创建用户个人数据库"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql0 = "CREATE TABLE IF NOT EXISTS data(username TEXT, password TEXT, created_time TEXT, latest_time TEXT)"
        sql1 = "CREATE TABLE IF NOT EXISTS data(url TEXT, key TEXT, info TEXT, created_time TEXT, change_time TEXT)"
        if type==0 :
            cursor.execute(sql0)
            if not self.is_has('admin'):  # 管理员的用户名一定为 admin ！
                created_time = self.get_time()
                default = "INSERT INTO data(username, password, created_time, latest_time) VALUES('admin', 'admin123', ?, ?)"  # 设置初始的账号密码
                cursor.execute(default, (created_time,created_time))
        elif type==1:
            cursor.execute(sql1)
        connect.commit()
        connect.close()

    def insert_table(self, username, password):
        """向后台数据库中插入元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        if self.is_has(username):
            print("已有该用户名（{}）".format(username))  # 打印日志
            return True  # 已经有该元素的时候返回一个 True 提供外界接口
        else:
            created_time = self.get_time()
            sql = 'INSERT INTO data (username, password, created_time) VALUES(?,?,?)'
            cursor.execute(sql, (username, password, created_time))
            connect.commit()
        connect.close()

    def insert_table1(self, url, key, info, created_time, change_time):
        """向后台数据库中插入元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'INSERT INTO data (url, key, info, created_time, change_time) VALUES(?,?,?,?,?)'
        cursor.execute(sql, (url, key, info, created_time, change_time))
        connect.commit()
        connect.close()

    def read_table(self, type=0):
        """读取数据库中的所有元素"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        if type==0:
            sql = 'SELECT * FROM data ORDER BY latest_time DESC'
        else:
            sql = 'SELECT * FROM data ORDER BY created_time'
        result = cursor.execute(sql)
        data = result.fetchall()
        connect.commit()
        connect.close()
        return data

    def update_table(self, username, password):
        """更新数据库中的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'UPDATE data SET password =? WHERE username=? '
        cursor.execute(sql, (password, username))
        connect.commit()
        connect.close()

    def update_time(self, username):
        """更新数据库中的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'UPDATE data SET latest_time =? WHERE username=? '
        cursor.execute(sql, (self.get_time(), username))
        connect.commit()
        connect.close()

    def update_table_by_time(self, info_db, key, info):
        """更新数据库中的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'UPDATE data SET ' + info_db + ' =? WHERE created_time=? '
        cursor.execute(sql, (info, key))
        connect.commit()
        connect.close()

    def find_password_by_username(self, username):
        """根据用户名来查找用户的密码"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = 'SELECT password FROM data WHERE username=?'
        result = cursor.execute(sql, (username,))
        connect.commit()
        found_data = result.fetchall()
        connect.close()
        return found_data

    def delete_table_by_username(self, info, type=0):
        """通过用户名称(type=0)或(type=1)删除数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql0 = 'DELETE FROM data WHERE  username=?'
        sql1 = 'DELETE FROM data WHERE  url=?'
        if type == 0:
            result = cursor.execute(sql0, (info,))
        elif type == 1:
            result = cursor.execute(sql1, (info,))
        connect.commit()
        connect.close()

    def is_has(self, info, type=0):
        """判断数据库中是否包含用户名信息（type=0）或网址（type=1）"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql0 = 'SELECT * FROM data WHERE username=?'
        sql1 = 'SELECT * FROM data WHERE url=?'
        if type==0:
            result = cursor.execute(sql0, (info,))
        elif type==1:
            result = cursor.execute(sql1, (info,))
        connect.commit()
        all_data = result.fetchall()
        connect.close()
        if all_data:
            return True
        else:
            return False

    def clear(self):
        """清空所有的数据"""
        connect = sqlite3.connect(self._database)
        cursor = connect.cursor()
        sql = "DELETE FROM data"
        cursor.execute(sql)
        connect.commit()
        connect.close()

    @staticmethod
    def get_time():
        """当前时间"""
        date = time.localtime()
        now_time = "{}-{}-{}-{}:{}:{:02d}.{:06d}".format(date.tm_year, date.tm_mon,
                                                  date.tm_mday,
                                                  date.tm_hour, date.tm_min,
                                                  date.tm_sec, datetime.now().microsecond)
        return now_time