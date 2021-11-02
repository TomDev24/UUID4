from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from shareFile.models import User

class RegForm(FlaskForm):
    username = StringField( "Username",
                            validators=[DataRequired(), Length(min=2, max=20)] )
    email = StringField( "Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                                validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField( "Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                            validators=[DataRequired()])
    submit = SubmitField("Log in")

class UploadFileForm(FlaskForm):
    filename = StringField( "File Name",
                            validators=[DataRequired(), Length(min=2, max=20)] )
    file = FileField("File", validators=[DataRequired()] )
    access_setting = SelectField('Privacy Setting', choices=[(2,"File open for everyone"), (1,"Link access"), (0,"Only for me")])
    submit = SubmitField("Upload File")
