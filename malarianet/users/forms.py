from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

from flask_login import current_user
from malarianet.models import User


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email(),DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Email(),DataRequired()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords don\'t match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def check_email(self,feild):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already registered! Try logging in!')

    def check_username(self,feild):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use. Try a different username!')
