from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserSignupForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField('Create my account')

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField('Submit Login')

class UpdateEmail(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit_button = SubmitField('Update My Email Address')

class AddWordForm(FlaskForm):
    word = StringField('Word', validators = [DataRequired()])
    submit_button = SubmitField('Add Word!')