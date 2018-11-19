from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
import os
from flask_migrate import Migrate
 
mail = Mail()
db = SQLAlchemy()
loginManager = LoginManager()
loginManager.login_view='auth.login'

def create_app(config_name='default'):
    config_name = os.getenv('flaskConfig')  or 'default'
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mail.init_app(app)
    db.init_app(app)
    loginManager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    migrate = Migrate(app, db)
    return app
