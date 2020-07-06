from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter your username"), Length(min=3, max=10)])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min=3, max=10)])
    remember = BooleanField('remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter a username"), Length(min=3, max=10)])
    email = StringField('Email', validators=[DataRequired("Please enter a valid email"), Length(min=3, max=40), Email("Email not valid")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password"), Length(min=3, max=10)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired("Please confirm password"), EqualTo('password')])
    submit = SubmitField('Sign Up')
