# Інтернет-магазин (by Flask)

## Склад команди:
>- [Юлія Кавуненко(Team Leader)](https://github.com/YuliiaKavunenko)
>- [Микола Єжов](https://github.com/mykolayezhov)
>- [Іван Єжов](https://github.com/EzhovIvan)
>- [Артем Мозговий](https://github.com/MozgoviyArtem)
>- [Артем Криворучка](https://github.com/Artem653) 
>- [Іван Іванов]()

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
#### Задаємо усі необхідні данні для відправлення повідомлень через gmail нашим користувачам
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
#### Створюємо менеджера для автентифікації наших користувачів, якщо вони вже були авторізовані
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
#### Створюємо усі необхідні таблиці у вигляді класу для подальшого використання

## Чому саме SQLite3?
### SQLite - це простий вбудований SQL-сервіс, який не вимагає окремого сервера. З ним доволі легко взаємодіяти безпосередньо з Python за допомогою модуля sqlite3. Саме ця база даних була нам більш зручною для використання у веб-додатку, а також у __Telegram-bot__, оскільки він підтримує SQL-запити Крім того, SQLite базу даних можна зберігати в одному файлі, що спрощує розгортання та роботу з нею. І важливо зазначити, що ми використовували бібліотеку flask_sqlalchemy для роботи з базами даних, через яку було дуже зручно налаштувати створення файлу і таблиць у базі даних. 

## Шаблоны HTML
### Registration page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('registration.static', filename = 'css/reg.css') }}">
    <script src = "{{ url_for('registration.static', filename = 'js/reg.js') }}" defer>
        
    </script>
{% endblock style %}

{% block title %}
    Registration
{% endblock %}

{% block content %}

    <a href="/registration/">REGISTRATION</a>

    <div class="background"></div>
    <!-- Форма створена для реєстрації користувача у базу данних -->
    <form method = "post" id = "reg_content">
        <p>Login</p>
        <input type="text" name = "login">
        <p>Email</p>
        <input type="email" name = "email">
        <p>Password</p>
        <input type="password" name = "password">
        <p>Password confirmation</p>
        <input type="password" name = "password confirmation">

        <button id="sendbutton" name = "senbutton">SEND</button>    

        <div class="firstmodal" id="firstModal">
            <div class="firstmodal-content">
                <h1>CONFIRMED</h1>
                <button id = "linkreg">
                    → AUTHORIZATION
                </button>
                    

            </div>
        </div>
              
    </form>

{% endblock %}
```
#### Створюємо елемент на нашій сторінці реєстрації з модальним вікном
### Authorization page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('auth.static', filename = 'css/auth.css') }}">
    <script src = "{{ url_for('auth.static', filename = 'js/auth.js') }}" defer></script>
{% endblock style %}

{% block title %}
    Authorization
{% endblock %}

{% block content %}

    <a href="/authorization/" id = "authorization">AUTHORIZATION</a>
    

    <div class="background"></div>
    <!-- Форма створена для авторизації користувача -->
    <form method = "post" id = "auth_content">
        <p>Login or email</p>
        <input type="text" name = "login">
        <p>Password</p>
        <input type="password" name = "password">
        <button id = "auth_button">SEND</button>
    </form>
    {% if error == True %}
        <div class = "modal" id = "modal_window">
            <div style="display: flex;" class = "modal_content">

                <p>YOU ARE NOT REGISTERED</p>
                <a id = "close" href="/registration/">
                    → REGISTRATION
                </a>
                <!-- <a href="/">→ HOME</a> -->
                
            </div>
        </div>
    {% elif error == False %}
        <script>
            window.onload() = function(){
                var modal = document.getElementById("modal_window");
                modal.style.display = "none";
                
            }
        </script>
    {% endif %}

{% endblock %}
```
#### Створюємо елемент на нашій сторінці авторізації з модальним вікном
### Home page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('home.static', filename = 'css/home.css') }}">
    <script  src = "{{ url_for('home.static', filename = 'js/home.js') }}" defer></script>
{% endblock style %}

{% block title %}
    Home Page
{% endblock %}

{% block content %}

    <p>Home Page</p>
    {% if name != "" %}
        <div class = "links">
            <a href="/" id= "linkhome">HOME</a>
            <a href="/shop/">SHOP</a>
            <a href="/cart/">            
                <div class = "basket">
                    CART 
                    <div class = "bgcounter" style="display: none;" id='basketcount' >
                        <p id = "counter" >1</p>
                    </div>
                </div>
            </a>
            <a href="/contacts/">CONTACTS</a>
            {% if is_admin == 'admin' %}
                <a href="/adminshop/">ADMIN</a>
            {% endif %}
        </div>
    {% endif %}
{% endblock %}
```
#### Створюємо елементи на нашій головній сторінці 
### Shop page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('shop.static', filename = 'css/shop.css') }}">
    <script  src = "{{ url_for('shop.static', filename = 'js/shop.js') }}" defer>

    </script>
{% endblock style %}

{% block title %}
    Shop
{% endblock %}

{% block content %}
    <h1>{{ name }}</h1>

    <div class = "links">
        <a href="/">HOME</a>
        <a href="/shop/">SHOP</a>
        <a href="/cart/">
            <div class = "basket">
                CART 
                <div class = "bgcounter" id="basketcount" style="display: none;" >
                    <p id = "counter">1</p>
                </div>
            </div>
            
        </a>
        <a href="/contacts/">CONTACTS</a>
        {% if is_admin == 'admin' %}
            <a href="/adminshop/">ADMIN</a>
        {% endif %}
    </div>
<!-- ☨ -->
    <div class = 'link_space'>

    </div>
    {% for products in product %}
    <div class = 'content'>
        <div class = "product">
            <img src="/../static/shopPage/img/{{ products.image }}" alt="НЕМАЭ ЗОБРАЖЕННЯ0">
            <div class="product_content">
                <h2>{{ products.name }}</h2>
                <h2 id="price">{{ products.price }} грн</h2>
                <h2 id = 'discount'>ЗНИЖКА {{ products.discount }}%</h2>
                <h2>{{  products.price - (products.price / 100 * products.discount) }} грн</h2>
                <form method = "post">
                    <button type="submit" class = "buy_button" id="{{ products.id }}" {% if products.count == 0 %}disabled{% endif %}>КУПИТИ</button>
                </form>
                <h3>{{ products.description }}</h3>
                <div class="КНОПКИ">
                    <form method="post">
                        {% for memory in products.memory.split(",") %}
                            <button type="submit" {% if products.count == 0 %}disabled{% endif %}>{{ memory }}</button>
                        {% endfor %}
                    </form>
                    
                </div>
                <div class="vnayavnosti">
                    
                    {% if products.count > 0 %}
                    <div class = 'confirm'><p>✓</p></div>
                    <p>ТОВАР В НАЯВНОСТІ</p>

                    {% else %}
                        <div class = 'notconfirm'></div>
                        <p id="notconfirmtext">НЕ В НАЯВНОСТІ</p>

                    {% endif %}
                    

                </div>
            </div>
            

        </div>
    </div>
        
        
    {% endfor %}

{% endblock %}

```
#### Додаємо усі продукти з нашого excel файлу, які також зберігаються у базі данних і додаємо робочі кнопки для додавання товару у кошик
### Cart page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('basket.static', filename = 'css/basket.css') }}">
    <script src="{{ url_for('basket.static', filename = 'js/basket.js') }}" defer></script>
{% endblock style %}

{% block title %}
    Basket
{% endblock %}

{% block content %}

    <h1>{{ name }}</h1>

    <div class = "links">
        <a href="/">HOME</a>
        <a href="/shop/">SHOP</a>
        <a href="/cart/">
            <div class = "basket">
                CART 
                <div class = "bgcounter" style="display: none;" id = 'basketcount' >
                    <p id = "counter" >1</p>
                </div>
            </div>
        </a>
        <a href="/contacts/">CONTACTS</a>
        {% if is_admin == 'admin' %}
            <a href="/adminshop/">ADMIN</a>
        {% endif %}
    </div>



    {% if products != "" %}

    <div id="basket_content" class="{% if user_order_status == 'wait_accept' %}basket_content_column{% else %}basket_content_row{% endif %}">
        {% if user_order_status == "wait_accept" %}
        <div class="acceptText">
             <h3>ВАШІ ДАНІ У ОБРОБЦІ</h3>
             <h3>КОНСУЛЬТАНТ ЗВ'ЯЖЕТЬСЯ З ВАМИ ДЛЯ ПІДТВЕРДЖЕННЯ ЗАМОВЛЕННЯ</h3>
        </div> 
     {% endif %}
        <div class="content">
            {% for product in products %}
                <div class="product_content">
                    <img src="/../static/shopPage/img/{{ product.image }}" alt="not found">
                    
                    <div class="product">

                        <div class="product_text">
                            <h2 id="product_name">{{ product.name }}</h2>
                            <div class="amount">
                                <form method="post">
                                    <button class="{% if user_order_status == 'wait_accept' %}minus_count_none{% else %}minus_count{% endif %}" id="{{ product.id }}">-</button>
                                </form>
                                <h2 class="{% if user_order_status == 'wait_accept' %}count_in_basket_fixed{% else %}count_in_basket{% endif %}">1</h2>
                                <form method="post">
                                    <button class="{% if user_order_status == 'wait_accept' %}plus_count_none{% else %}plus_count{% endif %}" id="{{ product.id }}">+</button>
                                </form>

                            </div>
                            <input type="hidden" name="discount" id="discount-{{ product.id }}" value="{{ product.discount }}">
                            <h2 class="product_price">{{ product.price }} грн</h2> 
                        </div>
                        <form method="post" class="bin">
                            <button class="bin_button"><img src="/../static/basketPage/img/bin.png" alt=""></button>
                        </form>
                    </div>
                </div>
                

            {% endfor %}
            </div>
            <div class="{% if user_order_status == 'wait_accept' %}чекаємо_оформлення{% else %}оформити{% endif %}">
                <!-- Форма створена для оновлення сторінки при відмовленні замовлення -->
                <form method="post">
                    <button class="{% if user_order_status == 'wait_accept' %}order_wait{% else %}order{% endif %}" >{% if user_order_status == 'wait_accept' %}ВІДМІНИТИ ЗАМОВЛЕННЯ{% else %}ПЕРЕЙТИ ДО ОФОРМЛЕННЯ{% endif %}</button>
                </form>
                <div class="{% if user_order_status == 'wait_accept' %}info_order_none{% else %}info_order{% endif %}">
                    <h3>4-и товари на суму</h3>
                    <h2>133 997 грн</h2>
                </div>
                

                <div class="{% if user_order_status == 'wait_accept' %}sale_none{% else %}sale{% endif %}">
                    <h3>Знижка</h3>
                    <h2>25 459 грн</h2>
                </div>
                
                
                <div class="total_sum">
                    <h3>Загальна сума</h3>
                    <h2>108 538 грн</h2>
                </div>
                
            </div>
            <div class = "background_form">
                <!-- Форма створена для оформлення замовлення -->
                <form method = "post" class = "make_order">
                    <h3>ОФОРМЛЕННЯ ЗАМОВЛЕННЯ:</h3>
                    <h4>ІМ'Я</h4>
                    <input type="text" name = "name" value="">
                    <h4>ПРІЗВИЩЕ:</h4>
                    <input type="text" name = "surname" value="">
                    <h4>ТЕЛЕФОН ЗАМОВНИКА:</h4>
                    <input type="text" name = "phone_number" value="">
                    <h4>EMAIL ЗАМОВНИКА:</h4>
                    <input type="text" name = "email" value="">
                    <h4>МІСТО ОТРИМУВАЧА:</h4>
                    <input type="text" name = "city" value="">
                    <h4>ВІДДІЛЕННЯ НОВОЇ ПОШТИ:</h4>
                    <input type="text" name = "nova_poshta" value="">
                    <h4>ДОДАТКОВІ ПОБАЖАННЯ:</h4>
                    <textarea type="text" name = "extra_info" value=""></textarea>
    
                    <button type = 'submit' id = "send_order">SEND</button>
                </form>
            </div>
            
        {% else %}
            <p>CART IS EMPTY</p>
        {% endif %}
    </div>
        
{% endblock %}

```
#### Отримуємо усі данні із cookie і завантажуємо через них данні продуктів у кошику
### Contacts page:
```html
{% extends "base.html" %}

{% block style %}
    <link rel="stylesheet" href="{{ url_for('contact.static', filename = 'css/contact.css') }}">
    <script  src = "{{ url_for('contact.static', filename = 'js/contact.js') }}" defer></script>
{% endblock %}

{% block title %}


{% endblock %}

{% block content %}
    <h1>{{ name }}</h1>


    <p>Contacts</p>
    <div class = "links">
        <a href="/">HOME</a>
        <a href="/shop/">SHOP</a>
        <a href="/cart/">
            <div class = "basket">
                CART 
                <div class = "bgcounter" style="display: none;" id = 'basketcount' >
                    <p id = "counter" >1</p>
                </div>
            </div>
        </a>
        <a href="/contacts/">CONTACTS</a>
        {% if is_admin == 'admin' %}
            <a href="/adminshop/">ADMIN</a>
        {% endif %}
    </div>
{% endblock %}
```
#### Додаємо усі елементи на сторінці контактів
### Admin page:
```html
{% extends "base.html" %}

{% block title %}
    Admin Shop
{% endblock %}


{% block style %}
    <link rel="stylesheet" href="{{ url_for('admin.static', filename='css/admin.css') }}">
    <script src = "{{ url_for('admin.static', filename = 'js/admin.js') }}" defer>

    </script>
{% endblock %}


{% block content %}
    <h1>{{ name }}</h1>

    <div class = "links">
        <a href="/">HOME</a>
        <a href="/shop/">SHOP</a>
        <a href="/cart/">
            <div class = "basket">
                CART 
                <div class = "bgcounter" id="basketcount" style="display: none;" >
                    <p id = "counter">1</p>
                </div>
            </div>

        </a>
        <a href="/contacts/">CONTACTS</a>
        
        {% if is_admin == 'admin' %}
            <a href="/adminshop/">ADMIN</a>
        {% endif %}

    </div>
<!-- ☨ -->
    <form method="post" class="add_form">
        <p>ДОДАТИ ПРОДУКТ</p>
        <button class="add_button" name="add_button">+</button>
    </form>

    <div class="background_modal1" style="display: none;">
        <div class="modal1">
            <!-- Форма створення для отримання данних нового продукту -->
            <form method="post" enctype="multipart/form-data" class="ZVOOZVOZVOZOVOZVOZXVO">
                <h4>NEW PRODUCT</h4>
                <h2>IMAGE PRODUCT:</h2>
                <input type="file" accept="image/*" name="image">
                <h2>NAME PRODUCT:</h2>
                <input type="text" name="name">
                <H2>DESCRIPTION PRODUCT:</H2>
                <textarea name="description" ></textarea>
                <h2>PRICE PRODUCT:</h2>
                <input type="number" name="price">
                <h2>DISCOUNT PRODUCT:</h2>
                <input type="number" name="discount">
                <h2>COUNT PRODUCT:</h2>
                <input type="number" name="count">
                <h2>MEMORY PRODUCT:</h2>
                <input type="text" name="memory">
                <button>SEND</button>
            </form>

        </div>
    </div>

    {% for products in product %}
    <div class = 'content'>
        <div class = "product">
            <!-- 1 -->
            <div id="edit_image">
                <img src="/../static/shopPage/img/{{ products.image }}" alt="НЕМАЭ ЗОБРАЖЕННЯ0">
                <!-- Форма створена для отримання данних нового зображення, його збереження -->
                <form method="post" enctype="multipart/form-data">
                    <input type="hidden" name="product_id"  value="{{ products.id }}">
                    <button class = "edit" id = 'edit-image-{{ products.id }}'>
                        <img src="{{ url_for('admin.static', filename = 'img/pencil.png') }}" alt="">
                    </button>
                    <div class = "background_modal">
                        <div id = "modal-image-{{ products.id }}" class = "modal" style = "display: none;">
                            <p>CHANGE IMAGE:</p>
                            <input type="file" name="new_image" accept="image/*" value="{{ products.name }}" id = "input-image-{{ products.id }}" style = "display: none;"">

                            <button class = 'save' id = 'save-image-{{ products.id }}' style = "display: none;">
                                SEND
                            </button>
                        </div>
                    </div>

                </form>
            
            </div>
            
            <div class="product_content">
                <div id="edit_name">
                    <h2 id = 'name-{{ products.id }}'>{{ products.name }}</h2>
                    
                   
                    <!-- Форма створенна для отримання данних нового ім'я продукту -->
                    <form method="post">
                        <input type="hidden" name = "product_id" value = "{{ products.id }}">
                        <button class="edit" id = 'edit-name-{{ products.id }}'>
                            <img src="{{ url_for('admin.static', filename = 'img/pencil.png') }}" alt="">
                        </button>
                        <div class = "background_modal">
                            <div id = "modal-name-{{ products.id }}" class = "modal" style = "display: none;">
                                <p>CHANGE NAME:</p>
                                <input type="text" name="new_name" value="{{ products.name }}" id="input-name-{{ products.id }}" style = "display: none;">
                                <button class = 'save' id = 'save-name-{{ products.id }}' style = "display: none;">
                                    SEND
                                </button>
                            </div> 
                        </div>

                    </form>
                </div>

                <div id="edit_price">
                    <h2 id="price">{{ products.price }} грн</h2>
                    <!-- Форма створена для отримання данних нової ціни продукту -->
                    <form method="post">
                        <input type="hidden" name = "product_id" value = "{{ products.id }}">
                        <button class="edit" id = 'edit-price-{{ products.id }}'>
                            <img src="{{ url_for('admin.static', filename = 'img/pencil.png') }}" alt="">
                        </button>
                        <div class = "background_modal">
                            <div id = "modal-price-{{ products.id }}" class = "modal" style = "display: none;">
                                <p>CHANGE PRICE:</p>
                                <input type="text" name="new_price" value="{{ products.price }}" id="input-price-{{ products.id }}" style = "display: none;">
                                <button class = 'save' id = 'save-price-{{ products.id }}' style = "display: none;">
                                    SEND
                                </button>
                            </div> 
                        </div>

                    </form>
                </div>


                <div id="edit_discount">
                    <h2 id="discount">ЗНИЖКА {{ products.discount }}%</h2>
                    <!-- Форма створена для отримання даних нової знижки продукту -->
                    <form method="post">
                        <input type="hidden" name = "product_id" value = "{{ products.id }}">
                        <button class="edit" id = 'edit-discount-{{ products.id }}'>
                            <img src="{{ url_for('admin.static', filename = 'img/pencil.png') }}" alt="">
                        </button>
                        <div class = "background_modal">
                            <div id = "modal-discount-{{ products.id }}" class = "modal" style = "display: none;">
                                <p>CHANGE DISCOUNT:</p>
                                <input type="text" name="new_discount" value="{{ products.discount }}" id="input-discount-{{ products.id }}" style = "display: none;">
                                <button class = 'save' id = 'save-discount-{{ products.id }}' style = "display: none;">
                                    SEND
                                </button>
                            </div> 
                        </div>

                    </form>
                </div>


                <!-- НЕТРОГАТЬ -->
                <h2>{{  products.price - (products.price / 100 * products.discount) }} грн</h2>
                


                <!-- НЕТРОГАТЬ -->
                <form method = "post">
                    <button type="submit" class = "buy_button" id="{{ products.id }}" {% if products.count == 0 %}disabled{% endif %}>КУПИТИ</button>
                </form>



                <h3>{{ products.description }}</h3>
                



                <div class="КНОПКИ">


                        {% for memory in products.memory.split(",") %}
                        <!-- Форма створенна для отримання нових данних параметрів -->
                        <form method="post">
                            <button class = 'memory' type="submit" {% if products.count == 0 %}disabled{% endif %} id = "memory-{{ loop.index0 }}-{{ products.id }}">{{ memory }}</button>
                            <input type="hidden" name = "index_button_{{ products.id }}" value = "{{ loop.index0 }}">
                            <input type="hidden" name = "product_id" value = "{{ products.id }}">

                            <button name="edit" class="edit" id = 'edit-memory-{{ products.id }}-{{ loop.index0 }}'>
                                <img src="{{ url_for('admin.static', filename = 'img/pencil.png') }}" alt="">
                            </button>
                            <div class = "background_modal">
                                <div id = "modal-memory-{{ products.id }}" class = "modal" style = "display: none;">
                                    <p>CHANGE MEMORY:</p>
                                    <input type="text" name="new_memory" value="{{ products.memory }}" id="input-memory-{{ products.id }}" style = "display: none;">
                                    <button class = 'save' id = 'save-memory-{{ products.id }}' style = "display: none;">
                                        SEND
                                    </button>
                                </div> 
                            </div>

                        </form>
                        {% endfor %}
                    
                    
                </div>


                <!-- Форма створенна для отримання id продукта котрий потрібно видалити -->
                <form method="post" class="delete">
                    <input type="hidden" name="delete_product_id" value="{{ products.id }}">
                    <button class="delete-button" id="delete-button-{{ products.id }}">
                        <img src="{{ url_for('admin.static', filename = 'img/bin.png') }}" alt="" style="width: 31px; height: 37px;">
                        <p>ВИДАЛИТИ ТОВАР</p>
                    </button>
                </form>
                
                
            </div>
            

        </div>
    </div>
        
        
    {% endfor %}

{% endblock %}
```
#### Додаємо усі продукти що є на сторінці shop і робочі кнопки через які можна редагувати данні продукту, нові данні задаються через модальні вікна
## Views.py
### Registration page:
```python
# імпортуємо віс необхідні модулі
import flask, flask_login
# імпортуємо нашу базу данних
from project.settings import db
# імпортуємо наш клас User
from .models import User
# створюємо функцію відображення сторінки реєстрації
def render_reg(): 
    # перевіряємо метод POST
    if flask.request.method == 'POST':
        # створюємо об'єкт класу User де задаємо значення для стовпців name, email, password, is_admin
        user = User(
            # задаємо значення для стовпця name з об'єкту login з форми
            name = flask.request.form['login'],
            # задаємо значення для стовпця email з об'єкту email з форми
            email = flask.request.form['email'],
            # задаємо значення для стовпця password з об'єкту password з форми
            password = flask.request.form['password'],
            # задаємо значення для стовпця is_admin з об'єкту is_admin з форми
            is_admin = 'admin'
        )
        
        try:
            # спорба додати користувача до бази данних
            db.session.add(user)
            # збереження усіх оновлень у базі данних
            db.session.commit()
            # здйснюємо редірект на сторінку автрізацій
            return flask.redirect('/authorization/')
        except:
            # повертаємо помилку якщо здійснення збереження данних у базу не виконано
            return 'Error'
    # повертаємо шаблон де задаємо файл html
    return flask.render_template(template_name_or_list = 'reg.html')
```
#### Створюємо роботу відображення сторінки реєстрації, якщо користувач реєструється то отримуємо усі надісланні данні і зберігаємо у базу данних
### Authorization page:
```python
# імпортуємо необхідні модулі
import flask, flask_login
# імпортуємо наш клас User
from reg_page.models import User
# створюємо функцію відображення сторінки авторизації
def render_auth(): 
    # перевіряємо метод POST
    if flask.request.method == "POST":
        # створюємо об'єкт класу User де зберігаємо данні користувача за його ім'ям і паролем
        users = User.query.filter_by(
            # задаємо за яким ім'ям фільтруємо клас User
            name = flask.request.form["login"],
            # задаємо за яким паролем фільтрємо клас User
            password = flask.request.form["password"]
        )
        # перевіряємо чи існує такий користувач
        if len(list(users)) == 0:
            # виводимо що помилка реєстрації
            print('ERROR REG')
            # повертаємо шаблон сторінки де вказуємо файл html і задаємо для змінної error значення True 
            return flask.render_template(template_name_or_list = 'auth.html', error = True)
        # якщо існує такий користувач 
        else:
            # виводимо що реєстрація пройшла успішно
            print('GOOD REG')
            # вказуємо якого користувача потрібно авторизувати
            flask_login.login_user(users[0])
            # здійснюємо redirect на сторінку home
            return flask.redirect("/")
        
    print('NONE REG')
    # повертаємо наш шаблон де вказуємо файл html і задаємо для змінної error значення False
    return flask.render_template(template_name_or_list = 'auth.html', error = False)

```
#### Створюємо роботу відображення сторінки авторізації, якщо користувач зареєстрований то перенапрявряємо його на головну сторінку, якщо ні, то виводимо модально вікно для переходу на сторінку реєестрації
### Home page:
```python
# Імпортуємо модулі Flask і Flask_login
import flask, flask_login
# Імпортуємо модуль Os
import os
# Створюємо функцію для відображення сторінки home
def render_home():
# Перевіряємо чи авторизований користувач за допомогую Flask-login
    if flask_login.current_user.is_authenticated:
# Отримуємо им'я користувача        
        user_name = flask_login.current_user.name
# Перевіряємо чи є поточний користувач адміністратором       
        is_admin = flask_login.current_user.is_admin
# Повертаємо шаблон сторінки 
        return flask.render_template(
# Відображаємо шаблон 'home_html'            
            template_name_or_list = 'home.html',
# Передаємо ім'я користувача у шаблон            
            name = user_name,
# Передаємо стату адміністратора у шаблон            
            is_admin = is_admin
        )
    
    else: 
# Якщо користувач не авторизований, ім'я буде пустим
        user_name = ""     
# Якщо користувач не авторизований, статус адмінітратора буде пустим    
        is_admin = ''
# Повертаємо шаблон сторінки    
        return flask.render_template(
# Відображаємо шаблон home_html            
            template_name_or_list = 'home.html',
# Передаємо пусте ім'я користувача у шаблон            
            name = user_name,
# Передаємо пустий статус адміністратора у шаблон            
            is_admin = is_admin
        )
```
#### Якщо користувач автроризований, то передаємо його ім'я до html файлу, якщо ні - зберігаємо порожню строку
### Shop page:
```python
# Імпортуємо Flask, Flask-Login, os і pandas
import flask, flask_login, os, pandas
# Імпортуємо модель Product з іншого модуля
from reg_page.models import Product
# Імпортуємо проект
import project
# Визначаємо функцію для видалення всіх продуктів з бази даних
def delete_all_products():
# Видаляємо всі записи з таблиці Product   
    Product.query.delete()
 # Зберігаємо зміни в базі даних
    project.db.session.commit()
 # Визначаємо функцію для відображення сторінки магазину
def render_shop():
# Викликаємо функцію для видалення всіх продуктів з бази даних
    delete_all_products()
# Перевіряємо, чи є поточний користувач адміністратором
    is_admin = flask_login.current_user.is_admin
# Отримуємо абсолютний шлях до файлу Excel з продуктами
    xl_path = os.path.abspath(__file__ + '/../../project/products_shop.xlsx')
# Зчитуємо файл Excel за вказаним шляхом
    xl_read = pandas.read_excel(

        io=xl_path,
# Задаємо відсутність заголовків
        header=None,
# Задаємо назви колонок
        names=["name", "description", "image", "count", "memory", "discount","price"]
    )

# Перевіряємо, чи таблиця продуктів порожня
    if Product.query.count() == 0:
# Перебираємо рядки зчитані з Excel-файлу
        for product in xl_read.iterrows():
# Отримуємо дані з поточного рядка
            row_data = product[1]
# Створюємо новий об'єкт продукту з даними з Excel-файлу
            products = Product(
                name = row_data["name"],
                description = row_data["description"],
                image =  row_data["image"],
                count = row_data["count"],
                memory = row_data["memory"],
                discount = row_data["discount"],
                price = row_data["price"]

                
            )
# Додаємо новий продукт до сесії бази даних
            project.db.session.add(products)
# Зберігаємо всі зміни у базі даних
        project.db.session.commit()
# Отримуємо ім'я поточного користувача
    user_name = flask_login.current_user.name
# Повертаємо шаблон сторінки "shop.html" для рендерингу
    return flask.render_template(template_name_or_list="shop.html", name = user_name, product = Product.query.all(), count = products.count, is_admin = is_admin)
```
#### Відображаємо усі продукти які є у excel файлі і зберігаємо їх до бази данних
### Cart page:
```python
# імпортуємо потрібні модулі
import flask, flask_login
# імпортуємо клас Product і клас Cart
from reg_page.models import Product, Cart
# імпортуємо клас Message з модулю flask_mail для створення повідомлень
from flask_mail import Message
# імпортуємо нашу базу данних
from project.settings import db
# імпортуємо об'єкт класу Mail для надсилання повідомлення
from project.mail_config import mail
# створюємо функцію відображення сторінки
def render_basket():
    # отримуємо данні стовпчика is_admin данного користувача
    is_admin = flask_login.current_user.is_admin
    # отримуємо данні стовпчика id данного користувача
    user_id = flask_login.current_user.id
    # отримуємо значення cookie під назвою "product" 
    cookie_value = flask.request.cookies.get("product")
    # ящко coockie існують 
    if cookie_value:
        # створюємо список id з наших cookie 
        list_id = cookie_value.split(' ')
        # створюємо список продуктів
        list_products = []
        # створюємо список для однакових id
        list_same_id = [] 
        # перебираємо список наших id і зберигаємо у змінну id 
        for id in list_id:
            # зберігаємо кількість продуктів по id 
            count_products = list_id.count(id)
            # перевіряємо якщо данного id немає у списку однакових id 
            if id not in list_same_id:
                # додаємо до списку продуктів значення продутку по id 
                list_products.append(Product.query.get(id))
                # у списку однакових id додаємо данне id 
                list_same_id.append(id)
                # звертаємось до останньго елементу списку продуктів і його кількість замінюємо на зачення кількості наших продуктів
                list_products[-1].count = count_products
        # перевірка на метод POST
        if flask.request.method == "POST":
            # перевірка на отримання данних елементу name з форми
            if flask.request.form.get("name"):
                # створюємо змінну для імені продукту яке замовляє користувач
                name_products_message = ''
                # створюємо список для імені продуктів
                name_products = []
                # перебираємо список продуктів и зберігаємо у змінні product
                for product in list_products:
                    # додаємо значення імені данного продукту 
                    name_products_message += f"{product.name}\n"
                    # додаємо до списку імені продуктів сам продукт
                    name_products.append(f'{product}')
                    # з'єднуємо список продуктів у строку для збереження змінні у базі данних
                    name_products_db = ",".join(name_products) 
                # створюємо об'єкт класу Cart
                cart = Cart(
                    # задаємо данні для стовпця id  таке ж саме як у користувача 
                    id = user_id,
                    # задаємо данні для стовпця name які отримуємо з елементу name у формі
                    name = flask.request.form.get("name"),
                    # задаємо данні для стовпця surname які отримуємо з елементу surname у формі
                    surname = flask.request.form.get("surname"),
                    # задаємо данні для стовпця phone_number які отримуємо з елементу phone_number у формі
                    phone_number = flask.request.form.get("phone_number"),
                    # задаємо данні для стовпця email які отримуємо з елементу email у формі
                    email = flask.request.form.get("email"),
                    # задаємо данні для стовпця city які отримуємо з елементу city у формі
                    city = flask.request.form.get("city"),
                    # задаємо данні для стовпця nova_poshta які отримуємо з елементу nova_poshta у формі
                    nova_poshta = flask.request.form.get("nova_poshta"),
                    # задаємо данні для стовпця extra_info які отримуємо з елементу extra_info у формі
                    extra_info = flask.request.form.get("extra_info"),
                    # задаємо данні для стовпця name_products які отримуємо змінної name_product_db
                    name_products = name_products_db,
                    # задаємо данні "wait_accept" для стовпця status
                    status = "wait_accept"
                )

                try:
                    # спроба додати нове значення до таблиці Cart
                    db.session.add(cart)
                    # зберігаємо у змінні бази данних
                    db.session.commit()
                    # створюємо повідомлення
                    msg = Message(
                        # задаємо назву для повідомлення
                        subject = "Your order!",
                        # задаємо отримувача повідомлення
                        recipients= [cart.email],  
                        # задаємо текст повідомлення
                        body = f'Вітаю, {cart.name}! Ваше замовлення: \n{name_products_message} \nуспішно оформлено!',
                        # задаємо пошту відправника
                        sender = 'kavunenko0911@gmail.com'
                    )
                    # надсилаємо наши повідомлення
                    mail.send(msg)
                except Exception as e:
                    # виводимо помилку
                    print(f"Помилка: {e}")
            # якщо POST запрос виконуєця без отримання данних елемента name
            else:
                # отримуємо данні з класу Cart по id користувача
                user_orders = Cart.query.filter_by(id = user_id).all()
                # перебираємо всі данні користувача і зберігаємо їх у змінну order
                for order in user_orders:
                    # змінюємо значення стовпця status на "cancell_by_user"
                    order.status = "cancell_by_user"
                    # виводимо замовлення
                    print(order)
                    
                try:
                    # зберигаємо зміну у базі данних
                    db.session.commit()
                except Exception as e:
                    # виводимо помилку
                    print(f"Помилка: {e}")
                
    # якщо данних cookie немає 
    else:
        # зберігаємо пустий список продуктів 
        list_products = ''
    # отримуємо данні з стовпця name данного користувача
    user_name = flask_login.current_user.name
    # отримуємо статус замовлення данного користувача
    user_order = Cart.query.filter_by(id=user_id).all()
    # якщо такі данні існують 
    if user_order:
        # обираємо останній елемент у списку замовлень
        user_order_status = user_order[-1]
    # якщо даних не існує 
    else:
        # задаємо пустий список статусів
        user_order_status = ''
    # повертаємо шаблон сторінки де вказуємо файл html і данні для змінних name, products, is_admin, user_order_status
    return flask.render_template(template_name_or_list="basket.html", name = user_name, products = list_products, is_admin = is_admin, user_order_status = str(user_order_status))
```
#### Якщо є додані продукти то відображаємо їх, якщо користувач оформляє замовлення, то змінюємо статус замовлення і надсилаємо йому email. Якщо відміняє замовлення, то також змінюємо статус
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
#### Відображаємо шаблон сторінки контактів
### Admin page:
```python
# Імпорт фласку
import flask
# Імпортуємо flask_login
import flask_login
# Імпортуємо модель проекту
from reg_page.models import Product
# Імпортуємо базу даних
from project.settings import db
# Імпортуємо пандас та ос для роботи з ексель таблицею
import pandas, os

# Створення функціїї відображення сторінки admin
def render_admin():
# Отримуємо дані з стовпчика is_admin зареєстрованого користувача і збреігаємо у змінну
    is_admin = flask_login.current_user.is_admin
# Перевірка чи є користувач адміністратором
    if is_admin == 'admin':
# Перевірка методу POST
        if flask.request.method == "POST":
# Отримуємо шлях до таблиці excel та зберігаємо його у змінну
            xl_path = os.path.abspath(__file__ + '/../../project/products_shop.xlsx')

# Зчитуэмо наші дані з ексель файлу
            xl_read = pandas.read_excel(
# Задаємо шлях до нашого ексель файлу
                io = xl_path,
# Вказуємо що в ексель файлі не буде відображатися назви стовпців
                header = None,
# Задаємо назви наших стовпців в ексель файлі
                names = ["name", "description", "image", "count", "memory", "discount","price"]
            )

# Отримуємо об'єкт з форми delete_product_id
            delete_product_id = flask.request.form.get("delete_product_id")
# Перевірка чи не є значення delete_product_id порожнім
            if delete_product_id != None:
# Отримуємо продукт який потрібно видалити по ID
                product_delete = Product.query.get(int(delete_product_id))
# Видаляємо з бази даних продукт
                db.session.delete(product_delete)
                # Зберігаємо зміни у базі даних
                db.session.commit()
            # Видаляє вказаний рядок з ексель файлу
                xl_read = xl_read.drop(int(delete_product_id) - 1)
            # отримуємо данні з елементу name у формі 
            name = flask.request.form.get("name")
            # отримуємо данні з елементу description у формі
            description = flask.request.form.get("description")
            # отримуємо данні з елементу image у формі
            image = flask.request.files.get("image")
            # отримуємо данні з елементу price у формі
            price = flask.request.form.get("price")
            # отримуємо данні з елементу discount у формі     
            discount = flask.request.form.get("discount")
            # отримуємо данні з елементу count у формі
            count = flask.request.form.get("count")
            # отримуємо данні з елементу memory у формі
            memory = flask.request.form.get("memory")
            # якщо всі необхідні данні існують 
            if name and description and image and price and discount and count and memory != None:
                # створюємо об'єкт класу Product
                new_product = Product(
                    # задаємо значення для стовпця name з змінної name 
                    name = name,
                    # задаємо значення для стовпця description з змінної description
                    description = description,
                    # задаємо значення для стовпця image з змінної image
                    image = image.filename,
                    # задаємо значення count стовпця name з змінної count
                    count = count,
                    # задаємо значення для стовпця memory з змінної memory
                    memory = memory,
                    # задаємо значення для стовпця discount з змінної discount
                    discount = discount,
                    # задаємо значення для стовпця price з змінної price
                    price = price
                )
                # додаємо нові данні до бази данних
                db.session.add(new_product)
                # зберігаємо усі змінu у базі данних
                db.session.commit()
                # зберігаємо отриманну картинку
                image.save(os.path.abspath(__file__ + f"/../../static/shopPage/img/{image.filename}"))
                # створюємо словарь із данними нового продукту
                new_product_data = {
                    # задаємо данні для ключа name 
                    "name": name,
                    # задаємо данні для ключа description 
                    "description": description,
                    # задаємо данні для ключа image
                    "image": image.filename,
                    # задаємо данні для ключа count
                    "count": count,
                    # задаємо данні для ключа memory 
                    "memory": memory,
                    # Задаємо данні для ключа discount
                    "discount": discount,
                    # Задаємо данні для ключа price 
                    "price": price
                }
                # додаємо до нашого excel файлу новий продукт 
                xl_read = xl_read._append(new_product_data, ignore_index = True)


            # отримуємо елемент product_id з форми 
            product_id = flask.request.form.get('product_id')
            # отримуємо елемент new_name з форми
            new_name = flask.request.form.get('new_name')
            # отримуємо елемент mew_price з форми
            new_price = flask.request.form.get('new_price')
            # отримуємо елемент new_discount з форми
            new_discount = flask.request.form.get('new_discount')
            # отримуємо елемент new_memory з форми
            new_memory = flask.request.form.get('new_memory')
            # отримуємо елемент new_image з форми
            new_image = flask.request.files.get("new_image")
            # якщо new_name існує 
            if new_name != None:
                # отримуємо данні продукту по id 
                product = Product.query.get(int(product_id))
                # задаємо нове ім'я для стовпця name продукту 
                product.name = new_name
                # додаємо нове ім'я продукту до excel файлу
                xl_read.loc[int(product_id)- 1, "name"] = new_name
            # якщо new_price існує 
            if new_price != None:
                # отримуємо данні продукту по id 
                product = Product.query.get(int(product_id))
                # задаємо нову ціну для стовпця price продукту
                product.price = new_price
                # додаємо нову ціну продукту до excel файлу
                xl_read.loc[int(product_id) - 1, "price"] = int(new_price)
            # якщо new_discount імснує
            if new_discount != None: 
                # отримуємо данні продукту по id 
                product = Product.query.get(int(product_id))
                #задаємо нову скидку стовпця discount продукту
                product.discount = new_discount
                # додаємо нову скидку продукту до excel файлу
                xl_read.loc[int(product_id) - 1, "discount"] = int(new_discount)
            # якщо new_image існує 
            if new_image != None:
                # отримуємо данні продукту по id 
                product = Product.query.get(int(product_id))
                # отримуємо ім'я нового фото
                file_name = new_image.filename
                # зберігаємо наше нове фото
                new_image.save(os.path.abspath(__file__ + f"/../../static/shopPage/img/{file_name}"))
                # задаємо нове ім'я для стовпця image продукту
                product.image = file_name
                # зберігаємо нове ім'я продукту до excel файлу
                xl_read.loc[int(product_id) - 1, "image"] = file_name
            # якщо new_memory існує
            if new_memory != None:
                # отримуємо данні продукту по id 
                product = Product.query.get(int(product_id))
                # отримуємо данні з форми в залежності від id продукту
                memory_index = int(flask.request.form.get(f"index_button_{product_id}"))
                # додаємо новий список де зберігаються параметри
                memories = product.memory.split(",")
                # в залежності від Id продукту встановлюємо нові параметри
                memories[memory_index] = new_memory
                # зберігаємо нові параметри до продукта  у базі данних
                product.memory = ",".join(memories)
                # зберігаємо нові параметри у excel файлі 
                xl_read.loc[int(product_id) - 1, "memory"] = product.memory
                # зберігаємо усі змінні у базі данних
                db.session.commit()
            # зберігаємо усі зміни у базі данних
            xl_read.to_excel(xl_path, index = False, header = None)
            # зберігаємо усі змінні у базі данних
            db.session.commit()
        # здійснюємо редірект на сторінку адміністратора
        flask.redirect("/adminshop/")
        # отримуємо данні з стовпця name данного користувача
        user_name = flask_login.current_user.name
        # повертаємо наш шаблон де задаємо наш html файл і данні для змінних product, name і is_admin 
        return flask.render_template(template_name_or_list = 'admin.html', product = Product.query.all(),name=user_name, is_admin = is_admin)
    else:
        # якщо користувач не є адміністратором то повертаємо текст помилки
        return "Ви не є адміністратором!"
``` 
#### Відображаємо шаблон сторінки, а якщо адміністратор вводить якісь зміни, то ці зміни зберігаються у базі данних, у файлі excel. Також при додаванні продуктів усі данні зберігаються.
## JavaScript!
### Registration page:
```js
pass
```
#### У данному коді ви можете побачити роботу модального вікна при успішній реєстрації
### Authorization page:
```js
pass
```
#### У данному коді ви можете побачити роботу модального вікна, якщо користувач не зареєстрований
### Home page:
```js
pass
```
#### У данному коді ви можете побачити роботу лічильника для кошика
### Shop page:
```js
pass
```
#### У данному коді ви можете побачити, як взаємодіє кнопка "купити" з лічильником кошика
### Cart page:
```js
pass
```
#### У данному коді ви можете побачити роботу збільшення і зменьшення товару, а також відображення модального вікна. Також підрахунок суми, суми з знижкою і суми без знижки і роботу лічильника кошика
### Contacts page:
```js
pass
```
#### У данному коді ви можете побачити роботу лічильника для кошика
### Admin page:
```js
pass
```
#### У данному коді ви можете побачити роботу відображення усіх модальних вікон при натисканні на відповідну кнопку
## Висновок
### Завдяки роботі над даним проєктом набули нових навичок у роботі з фреймворком flask і такими його розширеннями, як flask_mail, flask_login, flask_migrate і flask_sqlalchemy. Також покращили знання стосовно роботи з файлами excel, базою данних sqlite3 і такими мовами, як html, python, css. Окрім цього навчилися працювати з новою для нас мовою JavaScript. Отже, загалом можна сказати, що ми дізналися багато нового і корисного для нас.
