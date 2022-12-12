# --------------------服务器配置-----------------------
from app.configUtils import ConfigUtils
conf = ConfigUtils()
cf = conf.get_config()

DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(cf.get('database','DIALECT'), cf.get('database','DRIVER'), cf.get('database','USERNAME'), cf.get('database','PASSWORD'), cf.get('database','HOSTNAME'), cf.get('database','PORT'), cf.get('database','DATABASE'))
SQLALCHEMY_DATABASE_URI = DB_URI

# 取消警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_TRACK_MODIFICATIONS

# SECRET_KEY
SECRET_KEY = 'abcdefghijklmm'
