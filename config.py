class Config(object):
    SECRET_KEY = "1"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


CONFIG = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
