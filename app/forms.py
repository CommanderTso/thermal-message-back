from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired

class SubmitMessageForm(FlaskForm):
    message = TextField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')