import sys
import configparser
import os


class ConfigUtils:
    def __init__(self):
        config_path = os.path.join(os.path.abspath('.'), "app/ini/develop.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path, 'utf8')  # 读取配置文件

    def get_config(self):
        return self.cf
