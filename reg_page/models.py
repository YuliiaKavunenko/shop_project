# Імпортуємо модуль flask_login
import flask_login
# Імпортуємо базу даних
from project.settings import db

# Створюємо клас для зберігання даних користувача
class User(db.Model,flask_login.UserMixin):
# Створюємо стовпчик з Id користувача з унікальним ключем
    id = db.Column(db.Integer, primary_key = True)
# Створємо стовпчик з Ім'ям користувача
    name = db.Column(db.String(50), nullable = False)
# Створємо стовпчик у я кому буде пошта користувача
    email = db.Column(db.String(100), nullable = False)
# Створємо стовпчик з паролем користувача
    password = db.Column(db.String(100), nullable = False)
# Створення стовпчика який перевіряє чи є користувач адміністратором 
    is_admin = db.Column(db.String(100), nullable = False)

# Магічний метод який буде виводити ім'я користувача при звертанні до моделі
    def __repr__(self):
# Повертає рядок з ім'ям користувача 
        return f'Користувач - {self.name}'

# Створюємо клас зберігання даних товару
class Product(db.Model):
# Створюємо стовпчик з Id товару з унікальним ключем
    id = db.Column(db.Integer, primary_key = True)
# Створємо стовпчик з назвою товару
    name = db.Column(db.Text, nullable = False)
# Створємо стовпчик з описом товару
    description = db.Column(db.Text, nullable = False)
# Створємо стовпчик з зображеннім товару
    image = db.Column(db.Text, nullable = False)
# Створємо стовпчик з кількістю товару
    count = db.Column(db.Integer, nullable = False)
# Створємо стовпчик з ємністю товару
    memory = db.Column(db.Text, nullable = False)
# Створємо стовпчик зі знижкою товару
    discount = db.Column(db.Integer, nullable = False)
# Створємо стовпчик з ціною товару
    price = db.Column(db.Integer, nullable = False)
    
# Метод який буде виводити назву товару при звертанні до моделі
    def __repr__(self):
# Повертає рядок з ім'ям товару
        return f"{self.name}"

# Створюємо клас зберігання даних замовника
class Cart(db.Model):
# Створємо стовпчик з ID замовлення
    id_order = db.Column(db.Integer, primary_key = True)
# Створємо стовпчик з ID замовника
    id = db.Column(db.Integer, nullable = False)
# Створємо стовпчик з ім'ям замовника
    name = db.Column(db.Text, nullable = False)
# Створємо стовпчик з прізвищем замовника
    surname = db.Column(db.Text, nullable = False)
# Створємо стовпчик з номером телефону замовника
    phone_number = db.Column(db.Text, nullable = False)
# Створємо стовпчик з поштою замовника
    email = db.Column(db.Text, nullable = False)
# Створємо стовпчик з містом яке вказав замовник
    city = db.Column(db.Text, nullable = False)
# Створємо стовпчик з відділеням нової пошти, яку вказав замовник
    nova_poshta = db.Column(db.Text, nullable = False)
# Створємо стовпчик з додатковою інформацією, яку вказав замовник
    extra_info = db.Column(db.Text, nullable = False)
# Створємо стовпчик з даними про товар який замовив користувач
    name_products = db.Column(db.Text, nullable = False)
# Створємо стовпчик з статусом замовлення
    status = db.Column(db.Text, nullable = False)

# Метод який буде виводити ім'я користувача при звертанні до моделі
    def __repr__(self):
# Повертає рядок з статусом замовлення користувача 
        return f'{self.status}'
    