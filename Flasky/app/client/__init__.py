'''
	客户相关接口
'''
from flask import  Blueprint

client_api = Blueprint('client', __name__)

from . import client