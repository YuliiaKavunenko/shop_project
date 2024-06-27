import flask, flask_login
from reg_page.models import Product, Cart
from flask_mail import Message
from project.settings import db
from project.mail_config import mail

def render_basket():
    is_admin = flask_login.current_user.is_admin
    user_id = flask_login.current_user.id
    cookie_value = flask.request.cookies.get("product")
    if cookie_value:
        list_id = cookie_value.split(' ')
        list_products = []
        list_same_id = [] 
        for id in list_id:
            count_products = list_id.count(id)
            if id not in list_same_id:
                list_products.append(Product.query.get(id))
                list_same_id.append(id)
                list_products[-1].count = count_products
            print(f'LIST PRODUCTS -- {list_products}')
            

        if flask.request.method == "POST":
            if flask.request.form.get("name"):
                name_products_message = ''
                name_products = []
                print("POST запрос получен")
                for product in list_products:
                    name_products_message += f"{product.name}\n"
                    name_products.append(f'{product}')
                    name_products_db = ",".join(name_products) 
                print(name_products_message)
                print(name_products)
                print(name_products_db)
                cart = Cart(
                    id = user_id,
                    name=flask.request.form.get("name"),
                    surname=flask.request.form.get("surname"),
                    phone_number=flask.request.form.get("phone_number"),
                    email=flask.request.form.get("email"),
                    city = flask.request.form.get("city"),
                    nova_poshta = flask.request.form.get("nova_poshta"),
                    extra_info = flask.request.form.get("extra_info"),
                    name_products = name_products_db,
                    status = "wait_accept"
                )

                print(cart)

                try:
                    db.session.add(cart)
                    db.session.commit()

                    msg = Message(
                        subject= "Your order!",
                        recipients= [cart.email],  
                        body = f'Вітаю, {cart.name}! Ваше замовлення: \n{name_products_message} \nуспішно оформлено!',
                        sender = 'kavunenko0911@gmail.com'
                    )

                    mail.send(msg)
                except Exception as e:
                    print(f"Помилка: {e}")
            else:
                user_orders = Cart.query.filter_by(id=user_id).all()
                print(user_orders)
                for order in user_orders:
                    order.status = "cancell_by_user"
                    print(order)
                try:
                    db.session.commit()
                except Exception as e:
                    print(f"Помилка: {e}")
                
                
    else:
        list_products = ''
    user_name = flask_login.current_user.name

    user_order = Cart.query.filter_by(id=user_id).all()
    if user_order:
        user_order_status = user_order[-1]
    else:
        user_order_status = ''
    print(type(user_order_status))


    print(user_id)
    print(user_order_status)
    return flask.render_template(template_name_or_list="basket.html", name = user_name, products = list_products, is_admin = is_admin, user_order_status = str(user_order_status))