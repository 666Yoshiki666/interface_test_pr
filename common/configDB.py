#用于连接mysql数据操作

import pymysql #用于操作mysql
import readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db('host')
    username = localReadConfig.get_db('username')
    password = localReadConfig.get_db('password')
    port = localReadConfig.get_db('port')
    database = localReadConfig.get_db('database')
    config = {
        'host' : str(host),
        'user' : username,
        'passwd' : password,
        'port' : int(port),
        'db' : database
    }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            #创建连接
            self.db = pymysql.connect(**config)
            #创建游标
            self.cursor = self.db.cursor()
            print('Connect DB successfully!')
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        #执行sql并返回行数
        self.cursor.execute(sql, params)
        #提交，不然无法保存新建或者修改的数据
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        #获取下一行
        value = cursor.fetchone()
        return value

    def closeDB(self):
        #关闭游标
        self.cursor.close()
        #关闭连接
        self.db.close()
        print('Database closed!')