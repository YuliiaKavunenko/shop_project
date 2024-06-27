# імпортуємо модуль flask_login
import flask_login
# імпортуємо головний додаток
from .settings import shop
# імпортуємо наш класс User
from reg_page.models import User
# задаємо секретний ключ для головного додатку
shop.secret_key = '9898922787323'
# створюємо об'єкт класу login_manager який відповідає за автентифікацією усіх користувачів
login = flask_login.LoginManager(app =  shop)
# створюємо декоратор
@login.user_loader
# створюємо функцію для автентифікації користувача
def load(id):
    # повертаємо користувача по id
    return User.query.get(id)