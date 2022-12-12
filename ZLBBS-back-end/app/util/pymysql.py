import threading
from dbutils.pooled_db import PooledDB
import pymysql
from app.configUtils import ConfigUtils

conf = ConfigUtils()
cf = conf.get_config()
lock = threading.Lock()
pymysql.install_as_MySQLdb()


class MYSQLManager(object):
    # init
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # connect database
    def connect(self):
        # self.conn = mysql
        self.conn = PooledDB(
            creator=pymysql,
            maxconnections=6,
            mincached=2,
            maxcached=10,
            maxshared=10,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host=cf.get('database', 'HOSTNAME'),
            user=cf.get('database', 'USERNAME'),
            password=cf.get('database', 'PASSWORD'),
            database=cf.get('database', 'DATABASE'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        ).connection()
        self.cursor = self.conn.cursor()

    # search more data
    def get_list(self, sql, args=None):
        lock.acquire()
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        lock.release()
        return result

    # search one data
    def get_one(self, sql, args=None):
        lock.acquire()
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        lock.release()
        return result

    # modify data
    def modify(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multi_modify(self, sql, args=None):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    # create
    def create(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        last_id = self.cursor.lastrowid
        return last_id

    # delete one data
    def delete(self, sql, args=None):
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            return True
        except:
            self.conn.rollback()
            return False

    # close database
    def close(self):
        self.cursor.close()
        self.conn.close()

    # with
    def __enter__(self):
        return self

    # break with
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('mysql have closed')
        self.close()


mysql = MYSQLManager()
