# імпортуємо наш пакет сторінки home 
import home_page
# імпортуємо наш пакет сторінки registration
import reg_page
# імпортуємо наш пакет сторінки authorization
import auth_page
# імпортуємо наш пакет сторінки basket
import basket_page
# імпортуємо наш пакет сторінки shop
import shop_page
# імпортуємо наш головний додаток 
from .settings import shop
# імпортуємо наш пакет сторінки contacts
import contact_page
#імпортуємо наш пакет сторінки admin
import admin_page

# додаємо посилання для сторінки home, вказуємо функцію відображення сторінки і методи
home_page.home.add_url_rule(rule= "/", view_func= home_page.render_home, methods = ["GET", "POST"])
# додаємо посилання для сторінки authorization, вказуємо функцію відображення сторінки і методи
auth_page.auth.add_url_rule(rule= "/authorization/", view_func= auth_page.render_auth, methods = ["GET", "POST"])
# додаємо посилання для сторінки registraton, вказуємо функцію відображення сторінки і методи
reg_page.registration.add_url_rule(rule= "/registration/", view_func= reg_page.render_reg, methods = ['GET', 'POST'])
# додаємо посилання для сторінки basket, вказуємо функцію відображення сторінки і методи
basket_page.basket.add_url_rule(rule= "/cart/", view_func= basket_page.render_basket, methods = ["GET", "POST"])
# додаємо посилання для сторінки shop, вказуємо функцію відображення сторінки і методи
shop_page.shop_app.add_url_rule(rule= "/shop/", view_func= shop_page.render_shop, methods = ['GET', 'POST'])
# додаємо посилання для сторінки contacts, вказуємо функцію відображення сторінки і методи
contact_page.contact.add_url_rule(rule= "/contacts/", view_func= contact_page.render_contact, methods = ['GET', 'POST'])
# додаємо посилання для сторінки admin, вказуємо функцію відображення сторінки і методи
admin_page.admin.add_url_rule(rule= "/adminshop/", view_func= admin_page.render_admin, methods = ['GET', 'POST'])

# реєструємо додаток сторінки home у головному додатку
shop.register_blueprint(blueprint= home_page.home) 
# реєструємо додаток сторінки registration у головному додатку
shop.register_blueprint(blueprint= reg_page.registration) 
# реєструємо додаток сторінки authorization у головному додатку
shop.register_blueprint(blueprint= auth_page.auth) 
# реєструємо додаток сторінки basket у головному додатку
shop.register_blueprint(blueprint= basket_page.basket)
# реєструємо додаток сторінки shop у головному додатку
shop.register_blueprint(blueprint= shop_page.shop_app)
# реєструємо додаток сторінки contacts у головному додатку
shop.register_blueprint(blueprint= contact_page.contact)
# реєструємо додаток сторінки admin у головному додатку
shop.register_blueprint(blueprint= admin_page.admin)