from flask import Flask
from config import config
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from gevent import monkey
# gevent阻塞处理
monkey.patch_all()
mongod = PyMongo()
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    mongod.init_app(app)
    jwt.init_app(app)

    from .user import user  as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")

    from .city import city_api as city_blueprint
    app.register_blueprint(city_blueprint, url_prefix="/city")
    return app
