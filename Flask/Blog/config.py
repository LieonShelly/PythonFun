import os

MysqlURI = "mysql://root:123456@mysql:3306/blog" # mysql yml文中的容器名称
print('========MysqlURI=====', MysqlURI)
class Config:

        SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
        SQLALCHEMY_DATABASE_URI = MysqlURI
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')