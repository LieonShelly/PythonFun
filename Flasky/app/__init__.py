from flask import Flask
from config import config, CeleryConfig
from flask_jwt_extended import JWTManager
from flask_uploads import (UploadSet, configure_uploads, IMAGES,
                              UploadNotAllowed, patch_request_class)
from flask_mongoengine  import MongoEngine
from celery import Celery
from pymongo import MongoClient
# from gevent import monkey

mongod = MongoClient()
jwt = JWTManager()
photos = UploadSet('photos', IMAGES)
db = MongoEngine()
celery = Celery()
celery.config_from_object(CeleryConfig)
from .task import *


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    jwt.init_app(app)
    configure_uploads(app, photos)
    patch_request_class(app)
    # monkey.patch_all()

    from .user import user  as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")

    from .city import city_api as city_blueprint
    app.register_blueprint(city_blueprint, url_prefix="/city")

    from .file import file_api as file_blueprint
    app.register_blueprint(file_blueprint, url_prefix="/file")

    from .consle import consle_api as console_blueprint
    app.register_blueprint(console_blueprint, url_prefix="/consle")
  
    from .car import car_api as car_blueprint
    app.register_blueprint(car_blueprint, url_prefix='/car')

    from .task import task_api as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/task')
    return app
