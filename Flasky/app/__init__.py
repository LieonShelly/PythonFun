from flask import Flask
from config import config
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from gevent import monkey
from flask_uploads import (UploadSet, configure_uploads, IMAGES,
                              UploadNotAllowed, patch_request_class)
from mongoengine import *


# gevent阻塞处理
# monkey.patch_all()
mongod = PyMongo()
jwt = JWTManager()
photos = UploadSet('photos', IMAGES)

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # mongod.init_app(app)
    jwt.init_app(app)

    configure_uploads(app, photos)
    patch_request_class(app)

    connect('wanchebao')

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

    return app
