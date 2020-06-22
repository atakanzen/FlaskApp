from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField, TextAreaField
from wtforms.validators import DataRequired, email_validator, length, Email, InputRequired
from wtforms.fields.html5 import EmailField

class MyForm(FlaskForm):
	name = StringField('Name',[DataRequired(),InputRequired(), length(5,20,'Name can be 20 characters maximum.')])
	email = EmailField('E-mail',[InputRequired(), Email('Please enter a valid e-mail address.')])
	message = TextAreaField('Message',[InputRequired(),length(-1,150,'Message can be 150 characters maximum.')])
	submit = SubmitField('Send')