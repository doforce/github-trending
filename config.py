
class Config:
    SECRET_KEY = '8994944848dddj8493jhsfdfajskdlru9'

    REMOTE_SERVER = 'trendings'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = False


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
