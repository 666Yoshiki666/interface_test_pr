#用于定义日志格式

import logging
import threading
import os
from datetime import datetime
import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, 'result')
        #判断result目录是否存在
        if not os.path.exists(resultPath):
            #创建result目录
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime('%Y%m%d%H%M%S')))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #创建日志程序，可以指定名称
        self.logger = logging.getLogger()
        #设置此日志记录器的日志级别。等级必须是int或str
        self.logger.setLevel(logging.INFO)
        #格式化的日志记录写入磁盘文件，即日志记录文件
        handler = logging.FileHandler(os.path.join(logPath, 'output.log'))
        #设置格式字符串初始化格式化程序
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #设置此处理程序的格式化程序
        handler.setFormatter(formatter)
        #向此日志记录器添加指定的处理程序
        self.logger.addHandler(handler)

class MyLog:
    log = None
    #创建Lock()锁
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod#静态修饰
    def get_log():
        if MyLog.log is None:
            #锁定线程
            MyLog.mutex.acquire()
            MyLog.log = Log()
            #释放锁
            MyLog.mutex.release()
        return MyLog.log