from Blog import bcrypt, db, mail
from flask_mail import Message
from flask import current_app, url_for
from PIL import Image
import secrets
import os

def save_picture(form_picture):
    randam_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = randam_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def sende_email(user):
    token = user.get_rest_token()
    print(token)
    msg = Message('Password Reset Request',
                    sender='noreply@demo.com',
                    recipients=[user.email]
                )
    msg.body = f'''To reset your password, visit the following link:
    {url_for('user.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)
