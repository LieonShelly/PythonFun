from app import  db

class VerrifyStatus:
	checking = "checking"
	finish = "finish"


class User(db.Document):
	name = db.StringField()


