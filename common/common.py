import os
from xlrd import open_workbook#用于操作excel
from xml.etree import ElementTree
from common.Log import MyLog as Log
from common import configHttp
import readConfig

localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

#从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    xlsPath = os.path.join(readConfig.proDir, 'testFile', xls_name)
    #打开excel文件读取数据
    file = open_workbook(filename=xlsPath)
    '''
    #获取工作表方式
    sheets()[0] #通过索引顺序获取
    data.sheet_by_index(0) #通过索引顺序获取
    data.sheet_by_name(u'Sheet1') #通过名称获取
    '''
    #通过名称获取工作表
    sheet = file.sheet_by_name(sheet_name)
    '''
    nrows #获取行数
    ncols #获取列数
    '''
    #获取行数
    nrows = sheet.nrows
    for i in range(nrows):
        '''
        row_values() #获取整行
        col_values() #获取整列
        '''
        # 获取整行
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls

database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(readConfig.proDir, 'testFile', 'SQL.xml')
        tree = ElementTree.parse(sql_path)
        for db in tree.findall('database'):
            db_name = db.get('name')
            table = {}
            for tb in db.getchildren():
                table_name = tb.get('name')
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get('name')
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql