from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed, FileField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')
