from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


mail = Mail()
db = SQLAlchemy()
loginManager = LoginManager()
loginManager.login_view='auth.login'

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].initApp(app)
    mail.init_app(app)
    db.init_app(app)
    loginManager.init_app(app)
    return app
