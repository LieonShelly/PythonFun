from flask_mongoengine import *
from app import db



class CarBrand(db.Document):
    brand_id = db.StringField()
    name = db.StringField()
    letter = db.StringField()
    logo = db.StringField()

    meta = {"collection": 'CarBrand'}

