class Config(object):
    """项目的配置类"""

    SECRET_KEY = "1"
    # 数据库相关配置
    # 设置数据库的链接地址
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:python@localhost:3306/flask_1?charset=utf8'
    # 关闭追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """开发环境中的配置类"""
    # 开启调试模式
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:python@localhost:3306/flask?charset=utf8'


class ProductionConfig(Config):
    """生产环境(线上)中配置类"""
    # 配置生产环境中使用的配置类
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:python@localhost:3306/flask?charset=utf8'


APPCONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}





