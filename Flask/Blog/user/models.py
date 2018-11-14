from flask_login import login_manager
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from Blog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    print('load_user')
    return  User.query.get(int(user_id))

class Roles(db.Model):
     __tablename__="roles"
     id = db.Column(db.Integer, primary_key=True)
     users = db.relationship('User', backref="role")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def get_rest_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
