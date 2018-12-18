from flask import Blueprint

consle_api = Blueprint('consle', __name__)

from app.consle import consle
