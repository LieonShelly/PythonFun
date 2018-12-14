import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdfasdfasdasd23231'
    MAIL_SERVER = "smtp.163.com" #os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = 587 #int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = True #os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        #['true', 'on', '1']
    MAIL_USERNAME = "lieoncx@163.com"#os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = "lieon1992316"#os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <lieoncx@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    JWT_SECRET_KEY = "asdfasdfasdasd23231"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=0.5)
    JWT_HEADER_TYPE=None

    @staticmethod
    def initApp(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/wanchebao"
    MONGO_USERNAME = 'lieon',
    MONGO_PASSWORD = 'lieon1992316',

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/wanchebao"

class ProductionConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/wanchebao"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}