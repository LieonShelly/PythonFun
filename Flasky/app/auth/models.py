
from app import db

class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 3
    MODERATE = 8
    ADMIN = 16


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        super(Role, self.__init__(**kwargs)
        if self.permisions is None:
            self.permisions = 0

    def __repr__(self):
        return '<User %r>' % self.email
  
class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    defalt = db.Column(db.Boolean, defalt=False, index=True)
    permissions = db.Column(db.Integer)
     users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
         return '<Role %r>' % self.name
