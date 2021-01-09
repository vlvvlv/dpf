from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    userid = StringField('사용자아이디', validators=[DataRequired(), Length(min=5, max=50)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=2, max=50)])
    usertel = StringField('전화번호', validators=[DataRequired(), Length(min=10, max=50)])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    userid = StringField('사용자 ID', validators=[DataRequired(), Length(min=5, max=50)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
