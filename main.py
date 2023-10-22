from flask import Flask

from home_page import index_bp
from questions import question_bp
from users import user_bp

app = Flask(__name__)

# Настройки защиты формы
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "asgjkdhajksdh1231ht"

# Регистрация компонентов
app.register_blueprint(question_bp)
app.register_blueprint(user_bp)
app.register_blueprint(index_bp)

# Запуск
app.run()
