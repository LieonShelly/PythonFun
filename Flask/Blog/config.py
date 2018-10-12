import os

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD') 
DATABASE = 'blog'
USER = 'root'

class Config:
        SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
        SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@localhost/{database}' 
        '?unix_socket=/cloudsql/{connection_name}').format(
        user=USER, password=CLOUDSQL_PASSWORD, 
        database=DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME) 

        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')