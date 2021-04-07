from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired('제목은 필수 입력 항목 입니다.')])
    content = TextAreaField('Content', validators=[DataRequired('내용은 필수 입력 항목 입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired('내용은 필수 입력 항목입니다.')])