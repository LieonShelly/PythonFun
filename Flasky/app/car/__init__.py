from flask import Blueprint

car_api = Blueprint('car', __name__)

from app.car import caraccess
