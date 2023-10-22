from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired


# Форма для регистрации

class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя')])
    email = EmailField('Email', validators=[DataRequired('Заполните email')])
    password = PasswordField('Пароль', validators=[DataRequired('заполнить')])
    password2 = PasswordField('Подтвердите пароль', validators=[DataRequired('заполнить')])

    button = SubmitField('Зарегестироваться')


# Форма для входа
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired('заполнить')])
    password = PasswordField('Пароль', validators=[DataRequired('заполнить')])

    button = SubmitField('Войти')
