from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import json
import os
from flask_mail import Mail
from Blog.config import Config
import pymysql

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_manager = 'login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    pymysql.install_as_MySQLdb()
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from Blog.user.routes import user
    from Blog.post.routes import post
    from Blog.main.routes import main
    from Blog.errors.handlers import errors
    from Blog.create_db.routes import cretedb

    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(cretedb)

    return app
