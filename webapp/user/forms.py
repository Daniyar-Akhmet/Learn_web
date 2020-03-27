from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired #класс помогает избежать ручных проверок, автоматически проверяет введенные формы

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомни меня', default=True, render_kw={"class": "form-check-input"}) # галочка по умоланию установлена
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-secondary"})
