from flask import Blueprint, render_template, url_for

# Создаем приложение
index_bp = Blueprint('home_page', __name__)


# Создаем url
@index_bp.route('/')
def home_page():
    return render_template('index.html')
