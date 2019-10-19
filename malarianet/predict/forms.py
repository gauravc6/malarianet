from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from wtforms import ValidationError


class UploadImage(FlaskForm):
    picture = FileField("Upload an image...",validators=[FileAllowed(['png','jpg']),DataRequired()])
    submit = SubmitField("Classify")
