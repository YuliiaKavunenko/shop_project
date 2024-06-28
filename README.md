# Інтернет-магазин (by Flask)

## Склад команди:
>- [Юлія Кавуненко(Team Leader)](https://github.com/YuliiaKavunenko)
>- [Микола Єжов](https://github.com/mykolayezhov)
>- [Іван Єжов](https://github.com/EzhovIvan)
>- [Артем Мозговий](https://github.com/MozgoviyArtem)
>- [Артем Криворучка](https://github.com/Artem653) 
>- [Іван Іванов](https://github.com/Ivanov-ivan123)

## Опис проєкту

#### Наш проєкт, інтернет-магазин, виконує стандартні функції інтернет покупок з встроєнним _Telegam-bot_, за допомогою якого можна працювати з замовленнями і з самим сайтом. Окрім цього, адміністратор сайту може редагувати дані на сторінці _shop_.

### Використані мови:
### Python
#### Це основна мова програмування, за допомогою якої був створенний наш проєкт.
#### _Фреймворки, що використовувались:_ 
>- _Flask - основний фреймворк, за допомогою якого було створено сам проєкт і усі сторінки._
>- _pyTelegramBotAPI - фреймворк, за допомогою якого був створений Telegram-bot і усі його функції._
### Css
#### Мова, яку ми використовуємо для стилізації наших веб-сторінок. Приклад підключення css файлу до html:
```html
  <link rel="stylesheet" href="{{ url_for('home.static', filename = 'css/home.css') }}">
  <!-- url_for - функція, за допомогої якої ми підключаємо css файл, до html -->
  <!-- home - назва нашого Blueprint, до якого ми підключаємо стилі -->
  <!-- filename - шлях до файлу css -->
```
#### *ВАЖЛИВО!!! Файл css потрібно підключати в `<head>`, або у блоці, що був створений у шаблоні для тега `<head>`*
### Html
#### Мова розмітки, яку ми використовуємо для створення структури та вмісту наших веб-сторінок. Для створення базового шаблону введіть `doc!` у файлі html і натисніть `Enter`
### JavaScript 
#### Мова програмування, за допомогою якої ми можемо додати функціонування для об'єктів на нашій веб-сторінці. Приклад підключення файлу js до html:
```html
  <script  src = "{{ url_for('home.static', filename = 'js/home.js') }}" defer></script>
  <!-- url_for - функція, за допомогої якої ми підключаємо css файл, до html -->
  <!-- home - назва нашого Blueprint, до якого ми підключаємо js файл -->
  <!-- filename - шлях до файлу js -->
  <!-- defer - параметр, завдяки якому робота javascript коду відбувається тільки після завантаження html файлу -->
```
#### *ВАЖЛИВО!!! Файл js потрібно підключати в `<head>`, або у блоці, що був створений у шаблоні для тега `<head>`*

### Демоверсія проєкту...

## Наш проєкт - корисний

#### За допомогою нашого проєкту, можна дізнатися, як створити повноцінний вебсайт використовуючи модуль _Flask_. Окрім цього, дізнатися, як зробити роботу вашого вебсайту більш зручним і побачити робочий приклад.

+ _**Адмін-панель**_ - додаючі адмін-панель, яка допоможе вам з редагуванням сторінки одразу на сайті, зробить роботу на вашому сайті дуже зручною! (Побачити приклад роботи адмін-панелі можна на сторінці _admin_)  
+ _**Telegram-bot**_ - у нашому проєкті ви можете побачити, як можна об'єднати роботу проєкту _Flask_ з _Telegram-ботом_, за доопомгою якого можна обробляти замовлення, видаляти користувачів (або позбавляти їх прав адміністратора) і продукти, а також, додавати нові продукти. (Побачити приклад роботи можна у папці BotShop)
#### Також проєкт був дуже корисним для нас, як новачків у цьому напрямку, бо у ньому поєднані різні мови і робота з різними модулями. 

## Початок роботи

### Для роботи з проєктом потрібно завантажити наступні модулі:
+ _**Flask**_ - легкий фреймворк для веб-розробки на Python, який дозволяє створювати веб-додатки.
+ _**Flask-Migrate**_ - розширення, яке допомагає здійснювати міграції бази даних, він працює з _**Flask-SQLAlchemy**_.
+ _**Flask-SQLALchemy**_ - розширення для роботи з базами даних, воно спрощує використання SQLAlchemy для взаємодії з реляційними базами даних.
+ _**Flask-Login**_ - модуль для аутентифікації користувачів на веб-сайті flask, яке дозволяє не реєструватися повторно користувачам, які вже зареєструвалися.
+ _**Flask-Mail**_ - модуль, який допомагає відправляти електронні листи з проєктів flask. 
+ _**pandas**_ - бібліотека для роботи з даними, яка дозволяє зчитувати, обробляти та аналізувати таблиці даних (в нашому випадку таблиці excel).
+ _**openpyxl**_ - модуль, що дозволяє працювати з файлами excel у форматі xlsx для того, щоб зчитувати та записувати дані у таблиці excel.
+ _**pyTelebotAPI**_ - бібліотека для створення Telegram-ботів на Python для взаємодії з Telegram API.

### Для запуску проєкту на локальному сервері:
1. > Завантажте проєкт, як ZIP папку. Для цього вам необхідно натиснути на зелену кнопку "<> Code" ⇾ "Download ZIP".
2. > Завантажте усі модулі, які необхідно. Для цього запустіть термінал (натисніть `Win + R` ⇾ `cmd` ⇾ `Enter` (на windows) або `Cmd + Space` для виклика _Spotlight_, введіть `Terminal` ⇾ `Enter` (на macOS). Щоб завантажити необхідні модулі введіть `pip install {назва модуля}`.
3. >  Проведіть міграції. відкрийте термінал проєкта і перейдіть у папку проєкту, для цього введіть `cd project`. Далі потрібно вводити наступні команди:
```python
flask --app settings db init
# Ця команда потрібна для ініціалізації бази даних і створення папки міграцій
flask --app settings db migrate
# Ця команда потрібна для проведення міграцій
flask --app settings db upgrade
# Ця команда потрібна для застосування усіх змін у базі данних
```
4. > Далі перейдіть до файлу `manage.py` і запустіть його. Після цього перейдіть за посиланням <http://127.0.0.1:5000/>
5. > Готово!
### Для запуску _Telegram-bot_:
1. > Перейдіть у папку бота `BotShop`
2. > Перейдіть у файл `main.py` і запустіть його
3. > Готово!
### Для запуску проєкту на віддаленому сервері (pythonanywhere):
1. > Перейдіть за посиланням [PythonAnywhere](https://www.pythonanywhere.com/)
2. > Зареєструйтесь або увійдіть в обліковий запис (Для реєстрації натисніть на зелену кнопку `Start running Python online in less than a minute!` ⇾ `Create a begginer account!`)
3. > Перейдіть в розділ **Web** і натисніть **Add a new web app**
4. > Оберіть **Flask**
5. > Оберіть найновішу версію Python
6. > Перейдіть в розділ **Files**
7. > Відкрийте термінал (**New Console**) і виконайте:
```bash
git clone https://github.com/YuliiaKavunenko/shop_project.git
```
8. > Перейдіть в директорію проекту:
```bash
cd shop_project
```
9. > Створіть віртуальне оточення:
```bash
python3 -m venv {назва віртуального оточення}
```
10. > Активуйте віртуальне оточення:
```bash
source {назва віртуального оточення}/bin/activate
```
11. > Встановіть необхідні модулі для проєкту:
```bash
pip install {назва модуля}
```
12. > Проведіть міграції:
 ```python
flask --app settings db init
# Ця команда потрібна для ініціалізації бази даних і створення папки міграцій
flask --app settings db migrate
# Ця команда потрібна для проведення міграцій
flask --app settings db upgrade
# Ця команда потрібна для застосування усіх змін у базі данних
```
13. > В розділі **Web** відкрийте **WSGI configuration file**. В 16 строчці замініть на назву вашого додатку:
```python
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys

# add your project directory to the sys.path
project_home = '/home/YuliiaKavunenko/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from project.settings import shop as application  # тут импортуйте з файла settings назву вашого проєкту

```
14. > В розділі **Web** напишіть дійсний шлях до вашого віртуального оточення (**Enter path to a virtualenv, if desired**) і дійсний шлях до папки з проєктом (**Working directoty**, **Source code**)
15. > В розділі **Web** натисніть **Reload** для перезапуску веб-додатку
16. > Готово!


## Структура проєкту

картинка структуры

### Опис веб-сторінок:
#### _**Registration**_ - сторінка на котрій користувач може зареєструватися.
#### _**Authorization**_ - сторінка на котрій користувач може увійти в аккаунт
#### _**Home**_ - головна сторінка
#### _**Shop**_ - сторінка на котрій користувач може переглянути всі продукти і додати у корзину.
#### _**Cart**_ - сторінка корзини, де користувач може переглянути усі додані їм товари. Також тут він може змінити їхню кількість, видалити товар з корзини або оформити замовлення.
#### _**Contacts**_ - сторінка де можна додати контакти магазина.
#### _**Admin**_ - сторінка, де адміністратор може змінити певні данні у товара, видалити товар або додати новий.

## Приклад створення головного додатку:
```python
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
```
## Приклад створення додатку сторінки
```python
# імпорт flask
import flask
# створюємо додаток сторінки home
home = flask.Blueprint(
    # задаємо ім'я 
    name ='home',
    # задаємо ім'я пакету в якому знаходимося
    import_name = 'home_page',
    # вказуємо шлях до папки template
    template_folder= 'templates', 
    # шлях до папки static сторінки
    static_folder= '/../static/homePage',
    # задаємо посилання на папку static сторінки
    static_url_path= '/../static/homePage'
)
```
## Спосіб налаштування Blueprint у urls
```python
# імпортуємо наш пакет сторінки home 
import home_page
# імпортуємо наш головний додаток 
from .settings import shop

# додаємо посилання для сторінки home, вказуємо функцію відображення сторінки і методи
home_page.home.add_url_rule(rule= "/", view_func= home_page.render_home, methods = ["GET", "POST"])

# реєструємо додаток сторінки home у головному додатку
shop.register_blueprint(blueprint= home_page.home) 
```
## Опис файла settings
```python
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


```
## Опис файла mail_config
```python
# імпортуємо модуль flask_mail
import flask_mail
# імпортуємо класс Mail для з'єднання з SMTP сервером і надсилання повідомлень
from flask_mail import Mail
# імпортуємо наш основний додаток
from project.settings import shop
# вказуємо пошту з якою ми працюємо
shop.config["MAIL_SERVER"] = 'smtp.gmail.com'
# вказуємо порт
shop.config["MAIL_PORT"] = 587
# вказуємо шифрування TLS
shop.config["MAIL_USE_TLS"] = True
# вказуємо шифрування SSL
shop.config["MAIL_USE_SSL"] = False
# задаємо пошту з якої будуть надсилатись повідомлення
shop.config["MAIL_USERNAME"] = "kavunenko0911@gmail.com"
# задаємо згенирований пароль до аккаунту
shop.config["MAIL_PASSWORD"] = "xuuz xwgv jpwh tmad"
# створюємо об'єкт для надсилання повідомлень
mail = Mail(shop)

```
## Опис файла login_manager
```python
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
```
## Models.py
```python
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
    
```
## Чому саме SQLite3?
### мега обьяснение

## Шаблоны HTML
### Registration page:
```html
<p> PASS </p>
```
### Authorization page:
```html
<p> PASS </p>
```
### Home page:
```html
<p> PASS </p>
```
### Shop page:
```html
<p> PASS </p>
```
### Cart page:
```html
<p> PASS </p>
```
### Contacts page:
```html
<p> PASS </p>
```
### Admin page:
```html
<p> PASS </p>
```

## Views.py
### Registration page:
```python
pass
```
### Authorization page:
```python
pass
```
### Home page:
```python
pass
```
### Shop page:
```python
pass
```
### Cart page:
```python
pass
```
### Contacts page:
```python
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
```
### Admin page:
```python
pass
```

## JavaScript!
### Registration page:
```js
pass
```
### Authorization page:
```js
pass
```
### Home page:
```js
pass
```
### Shop page:
```js
pass
```
### Cart page:
```js
pass
```
### Contacts page:
```js
pass
```
### Admin page:
```js
pass
```

## Висновок

