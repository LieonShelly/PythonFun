'''
城市列表相关接口
'''

from flask import Blueprint

city_api = Blueprint('city', __name__)

from . import city


