import telebot, os, pandas
import modules.data_base as m_data
import modules.create_keyboard as c_keyboard

user_id = ""
user_data = {}

@m_data.bot.callback_query_handler(func = lambda call: call.data == "get_users")

def callback_inline(call):
    m_data.cursor.execute("SELECT id, name, password, is_admin FROM user")
    users = m_data.cursor.fetchall()
    print(users)
    for user in users:
        m_data.bot.send_message(
            chat_id =  -1002196622948,
            text = f'''
ID:{user[0]}
Name:{user[1]}
Password:{user[2]}
➡️Is_dmin:{user[3]} 👾
            ''',
            reply_markup = c_keyboard.keyboard_edit_user,
            message_thread_id = 2
        )

@m_data.bot.callback_query_handler(func = lambda call: call.data == "delete_user")

def delete_user(call):
    global user_id
    user_data = call.message.text.split("\n")
    print(user_data)
    user_id = ",".join(user_data).split(":")[1].split(",")[0]

    print(user_id)
    if user_id:
        m_data.bot.send_message(
            chat_id =  -1002196622948,
            message_thread_id = 2,
            text = f"Ви дійсно хочите видалити користувача з id: {user_id}?",
            reply_markup = c_keyboard.keyboard_accept_del
        )

@m_data.bot.callback_query_handler(func = lambda call: call.data == "accept_user_del")

def accept_delete_user(call):
    global user_id
    m_data.cursor.execute("DELETE FROM user WHERE id = ?", (user_id,))
    m_data.connection.commit()
    m_data.bot.send_message(
        chat_id =  -1002196622948,
        message_thread_id = 2,
        text = f"Успішно видалено користувача з id: {user_id}"        
    )

@m_data.bot.callback_query_handler(func = lambda call: call.data == "remove_admin")

def remove_admin(call):
    user_data = call.message.text.split("\n")
    user_id = ",".join(user_data).split(":")[1].split(",")[0]
    m_data.cursor.execute("UPDATE user SET is_admin = ? WHERE id = ?",("user",user_id))
    m_data.connection.commit()
    m_data.bot.send_message(
        chat_id = -1002196622948,
        message_thread_id = 2,
        text = f"Користувач з id: {user_id} більше не адмін"
    )

@m_data.bot.callback_query_handler(func = lambda call: call.data == "get_products")

def get_products(call):
    m_data.cursor.execute("SELECT id, name, price FROM product")
    product_data = m_data.cursor.fetchall()
    for product in product_data:
        m_data.bot.send_message(
            chat_id =  -1002196622948,
            message_thread_id = 5,
            text = f'''
id:{product[0]}
name:{product[1]}
price:{product[2]}
''',
        reply_markup = c_keyboard.del_product_keyboard
    )
        
@m_data.bot.callback_query_handler(func = lambda call: call.data == "delete_product")

def delete_product(call):
    product_data = call.message.text.split("\n")
    product_id = product_data[0].split(":")[1]
    m_data.cursor.execute("DELETE FROM product WHERE id = ?",(product_id,))
    m_data.connection.commit()
    
    xl_read = pandas.read_excel(
        io = m_data.xl_path,
        header=None,
        names=["name", "description", "image", "count", "memory", "discount","price"]
    )

    xl_read = xl_read.drop(int(product_id) - 1)

    xl_read.to_excel(m_data.xl_path, index = False, header = None)


    m_data.bot.send_message(
        chat_id = -1002196622948,
        message_thread_id = 5,
        text =f"Продукт з id: {product_id} видалено"
    )

@m_data.bot.callback_query_handler(func = lambda call: call.data == "add_product")

def add_product(call):
    m_data.bot.send_message(
        chat_id = -1002196622948,
        message_thread_id = 194,
        text = "Надішліть фотографію продукту"
    )
    m_data.bot.register_next_step_handler(message = call.message, callback = save_photo)

def save_photo(message):
    if message.content_type == "photo":
        photo = message.photo[-1]
        print(message.photo)

        file_info = m_data.bot.get_file(photo.file_id)

        downloaded_file = m_data.bot.download_file(file_info.file_path)
        filename = os.path.basename(file_info.file_path)
        path = os.path.abspath(__file__ + f"/../../../static/shopPage/img/{filename}")
        with open(path, 'wb') as new_file:
            new_file.write(downloaded_file)

        user_data["photo_name"] = filename
        m_data.bot.send_message(chat_id= -1002196622948, text="Вкажіть ім'я продукту", message_thread_id = 194)
        m_data.bot.register_next_step_handler(message = message, callback = save_name)
    else:
        m_data.bot.reply_to(message = message, text="Будь ласка, надішліть фотографію")
        m_data.bot.register_next_step_handler(message = message, callback = save_photo)

def save_name(message):
    user_data["name"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id= -1002196622948, text="Вкажіть ціну продукту", message_thread_id = 194)
    m_data.bot.register_next_step_handler(message = message, callback = save_price)

def save_price(message):
    user_data["price"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id = -1002196622948, text="Вкажіть знижку для продукта", message_thread_id = 194)
    m_data.bot.register_next_step_handler(message = message, callback = save_discount)

def save_discount(message):
    user_data["discount"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id = -1002196622948, text="Вкажіть опис продукту", message_thread_id = 194)
    m_data.bot.register_next_step_handler(message = message, callback = save_description)

def save_description(message):
    user_data["description"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id = -1002196622948, text="Вкажіть кількість продукту", message_thread_id = 194)
    m_data.bot.register_next_step_handler(message = message, callback = save_memory)

def save_memory(message):
    user_data["count"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id = -1002196622948, text="Вкажіть параметри продукту", message_thread_id = 194)
    m_data.bot.register_next_step_handler(message = message, callback = save_count)

def save_count(message):
    user_data["memory"] = message.text
    print(message.text)
    m_data.bot.send_message(chat_id = -1002196622948, text=f"{user_data['name']} успішно додано до бази даних!", message_thread_id = 194)

    print('добавляем продукт..')
    print(user_data)
    m_data.cursor.execute('''
    INSERT INTO product (name , description, image, count, memory, discount, price) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_data['name'], user_data['description'], user_data['photo_name'], user_data['count'], user_data['memory'], user_data['discount'], user_data['price']))
    m_data.connection.commit()

    

    xl_read = pandas.read_excel(
        io = m_data.xl_path,
        header=None,
        names=["name", "description", "image", "count", "memory", "discount","price"]
    )
    new_product_data = {
        "name": user_data['name'],
        "description": user_data['description'],
        "image": user_data['photo_name'],
        "count": user_data['count'],
        "memory": user_data['memory'],
        "discount": user_data['discount'],
        "price": user_data['price']
                
    }
    xl_read = xl_read._append(new_product_data, ignore_index = True)
    xl_read.to_excel(m_data.xl_path, index = False, header = None)

@m_data.bot.callback_query_handler(func = lambda call: call.data == "cart")

def get_cart(call):
    m_data.cursor.execute("SELECT id, name, surname, phone_number, email, city, nova_poshta, extra_info, name_products, status FROM cart")
    cart_users_info = m_data.cursor.fetchall()
    print(cart_users_info)
    print(cart_users_info)
    for cart_user in cart_users_info: 
        m_data.bot.send_message(
            chat_id = -1002196622948,
            message_thread_id = 7,
            text = f'''
ORDER INFO:
Id:{cart_user[0]}
Customer name:{cart_user[1]}
Customer surname:{cart_user[2]}
Phone number:{cart_user[3]}
Email:{cart_user[4]}
City:{cart_user[5]}
Nova poshta:{cart_user[6]}
Extra informayion:{cart_user[7]}
PRODUCTS
{cart_user[8]}
STATUS:{cart_user[9]}
''', 
            reply_markup = c_keyboard.keyboard_order
        )
@m_data.bot.callback_query_handler(func = lambda call: call.data == "delete_order")

def delete_order(call):
    message_data = call.message.text.split("\n")
    order_id = message_data[1].split(":")[1]
    m_data.cursor.execute("DELETE FROM cart WHERE id = ?", (order_id,))
    m_data.connection.commit()
    m_data.bot.send_message(chat_id = -1002196622948, text = f"Ви видалили замовлення з ID {order_id}", message_thread_id = 7)

@m_data.bot.callback_query_handler(func = lambda call: call.data == "accept_order")

def accept_order(call):
    message_data = call.message.text.split("\n")
    order_id = message_data[1].split(":")[1]
    m_data.cursor.execute("UPDATE cart SET status = ?", ("accept",))
    m_data.connection.commit()
    m_data.bot.send_message(chat_id = -1002196622948, text = f"Ви прийняли замовлення з ID {order_id}", message_thread_id = 7)