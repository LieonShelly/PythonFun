import os

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD') 
DATABASE = 'blog'
USER = 'root'

DB4_PORT_3306_TCP_ADDR = os.environ.get('DB4_PORT_3306_TCP_ADDR') 
DB4_PORT_3306_TCP_PORT = os.environ.get('DB4_PORT_3306_TCP_PORT') 
DB4_ENV_MYSQL_ROOT_PASSWORD = os.environ.get('DB4_ENV_MYSQL_ROOT_PASSWORD') 
# mysql+pymysql://root:password@localhost:3306/test
MysqlURI = "mysql://root:{DB4_ENV_MYSQL_ROOT_PASSWORD}@{DB4_PORT_3306_TCP_ADDR}:{DB4_PORT_3306_TCP_PORT}/blog".format(DB4_ENV_MYSQL_ROOT_PASSWORD=DB4_ENV_MYSQL_ROOT_PASSWORD,DB4_PORT_3306_TCP_ADDR=DB4_PORT_3306_TCP_ADDR,DB4_PORT_3306_TCP_PORT=DB4_PORT_3306_TCP_PORT)
print('========MysqlURI=====', MysqlURI)
class Config:

        SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
        SQLALCHEMY_DATABASE_URI = MysqlURI
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')