#用于读取config配置文件中的内容

import os#操作系统功能
import codecs#编码转换
import configparser#读取写入配置文件

'''
os.path：用于文件的属性获取
'''
#split：将path分割成目录和文件名二元组返回
#realpath：返回的是 使用软链 的真实地址
#abspath：返回目标地址
#proDir = os.path.split(p=)[0]
proDir = os.path.realpath(path='D:\pycharm\interface_test_pr')
#join：连接两个或更多的路径名组件
configPath = os.path.join(proDir, "config")

class ReadConfig:

    def __init__(self):
        '''
        open()：打开文件
        read()：文件操作
        close()：关闭文件
        '''
        #打开文件
        fd = open(file=configPath, mode='r', encoding='utf-8')
        #操作文件-读取
        data = fd.read()

        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[:3]
            #codecs.open：读入时直接解码
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        #关闭文件
        fd.close()

        #初始化实例
        self.cf = configparser.ConfigParser()
        #读取配置文件
        self.cf.read(filenames=configPath, encoding='utf-8')

    '''
    cf.sections()：获取section返回list，即配置文件[]内容
    cf.options('section名')：获取section下的option返回list，即section下的key
    cf.items('section名')：获取section下的键值对返回list
    cf.get('section名', 'option名')：获取对应value
    '''
    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
