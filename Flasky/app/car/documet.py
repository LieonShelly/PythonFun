from mongoengine import *
from mongoengine import EmbeddedDocument
from mongoengine import StringField
from mongoengine import Document


class CarBrand(Document):
    brand_id = StringField()
    name = StringField()
    letter = StringField()
    logo = StringField()

    meta = {"collection": 'CarBrand'}

