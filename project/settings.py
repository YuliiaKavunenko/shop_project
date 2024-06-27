# імпортуємо всі модулі які нам потрібні
import flask, flask_sqlalchemy, flask_migrate, os
# створюємо наш головний додаток
shop = flask.Flask(
    # задаємо ім'я файла в якому знаходимось
    import_name = 'settings', 
    # вказуємо шлях до папки template
    template_folder = 'project/templates',
    # задаємо шлях для бази данних
    instance_path = os.path.abspath(__file__ + '/..'),
    # вказуємо шлях до папки static
    static_folder = 'static'
)
# вказуємо з якою базою данних ми працюємо
shop.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# створюємо базу данних
db = flask_sqlalchemy.SQLAlchemy(app  = shop)
# створюємо міграції для бази данних
migrate = flask_migrate.Migrate(app = shop, db = db)

