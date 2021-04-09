from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired('제목은 필수 입력 항목 입니다.')])
    content = TextAreaField('Content', validators=[DataRequired('내용은 필수 입력 항목 입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired('내용은 필수 입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('Check Password', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])