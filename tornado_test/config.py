import os

BaseDir = os.path.dirname(__file__)
# handlers设置
settings = {
    'static_path':os.path.join(BaseDir, 'static'),
    'template_path':os.path.join(BaseDir, 'template'),
    'xsrf_cookie':True,
    'debug':True,
    'cookie_secret':'HMNmfR5GR1CcxIRiUaA5T1MvcTC8EU1FrdIuGrSfb2U='
}

# 数据库设置
mysql = dict(
    host = '127.0.0.1',
    database = 'ihome',
    user = 'root',
    password = '123456.',
)

# 日志
log_level = 'debug'
log_file = os.path.join(BaseDir,'logs/log')