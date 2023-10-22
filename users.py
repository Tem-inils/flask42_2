from flask import Blueprint, session, render_template, url_for
from forms import RegisterForm, LoginForm

# Создаем приложение
user_bp = Blueprint('user', __name__, url_prefix='/user')


# Создаем url
@user_bp.route('/')
def home_user():
    return render_template('home_user.html')


# Регистрация
@user_bp.route('/register-user')
def register_user():
    form = RegisterForm()

    return render_template('registration.html', form=form)


# Логин
@user_bp.route('/login-user')
def login_user():
    form = LoginForm()

    return render_template('login.html', form=form)
