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
