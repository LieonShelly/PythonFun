from flask import Blueprint

file_api = Blueprint('file', __name__)

from app.file import file