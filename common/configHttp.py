#用于访问接口

import requests#使用Apache2 licensed 许可证的HTTP库
import readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http('url')
        port = localReadConfig.get_http('port')#config文件字段值为空,不可取
        timeout = localReadConfig.get_http('timeout')

        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def get(self):
        try:
            #get请求返回response
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            return response
        except:
            self.logger.error('Time Out!')
            return None

    def post(self):
        try:
            #post请求返回response
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except:
            self.logger.error('Time Out!')
            return None
