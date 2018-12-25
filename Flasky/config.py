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
    UPLOADED_FILES_DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'picture')
    UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'picture')
    MONGODB_DB = 'wanchebao'
    MONGODB_HOST = '127.0.1'
    MONGODB_PORT = 27017
    # MONGODB_USERNAME = 'root'
    # MONGODB_PASSWORD = 'lieon1992316'

    @staticmethod
    def initApp(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
 

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    MONGO_URI = "mongodb://localhost:27017/wanchebao"

class CeleryConfig:
    broker_url = 'redis://localhost:6379/2'
    result_backend = 'redis://localhost:6379/3'
    imports = ('app.task')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}