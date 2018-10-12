from flask import Blueprint
from Blog import db, create_app

cretedb = Blueprint('cretedb', __name__)

@cretedb.route("/cretedb")
def create_db():
    db.create_all()
    return "create all success"
    
