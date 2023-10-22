from flask import Blueprint

# Создаем приложение
question_bp = Blueprint('question', __name__, url_prefix='/question')


# Создаем url
@question_bp.route('/')
def home_question():

    return 'Hello Question Component'


