# імпорт flask
import flask
# імпорт flask_login
import flask_login
# створюємо функцію для відображення сторінки
def render_contact():
    # отримуємо дані із стовпця is_admin даного користувача
    is_admin = flask_login.current_user.is_admin
    # отримуємо дані із стовпця name даного користувача
    user_name = flask_login.current_user.name
    # Повертаємо шаблон нашої сторінки і зберігаємо для файлу html змінні name та is_admin
    return flask.render_template(template_name_or_list = 'contact.html', name = user_name, is_admin = is_admin)