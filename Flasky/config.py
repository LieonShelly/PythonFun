import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('secretKey')
    mailServer = os.environ.get('mailServer')
    mailPort = os.environ.get('mailPort')
    mailUseTls = os.environ.get('mailUseTls')
    mailUsername = os.environ.get('mailUsername')
    mailPasword = os.environ.get('mailPasword')
    flaskyMailSubjectPrefix = '[Flasky]'
    flaskyMailSender = 'Flasky Admin'
    flaskyAdmin = os.environ.get('flaskyAdmin')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def initApp(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}