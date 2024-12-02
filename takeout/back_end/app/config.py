class Config(object):
    """ 后端配置信息 """

    # 数据库的配置
    DIALCT   = "mysql"
    DRITVER  = "pymysql"
    HOST     = '127.0.0.1'
    PORT     = "3306"
    USERNAME = "root"
    PASSWORD = "040710hong" # 数据库的密码
    DBNAME   = 'takeout'

    SQLALCHEMY_DATABASE_URI = f"{DIALCT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 上传文件的配置
    UPLOAD_FOLDER = 'uploads'
