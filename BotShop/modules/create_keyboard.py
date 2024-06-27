# import create_buttons as c_buttons
import telebot
from telebot import types
import modules.data_base as m_data

get_users = types.InlineKeyboardButton(text = 'GET USERS', callback_data = "get_users")
get_products = types.InlineKeyboardButton(text = 'GET PRODUCTS', callback_data = "get_products")
add_product = types.InlineKeyboardButton(text = 'ADD PRODUCT', callback_data = "add_product")
cart = types.InlineKeyboardButton(text = 'CART', callback_data = "cart")

keyboard_menu = types.InlineKeyboardMarkup()
keyboard_menu.add(get_users)
keyboard_menu.add(get_products)
keyboard_menu.add(add_product)
keyboard_menu.add(cart)

delete = types.InlineKeyboardButton(text = "DELETE", callback_data = "delete_user")
remove_admin = types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = "remove_admin")

keyboard_edit_user = types.InlineKeyboardMarkup()
keyboard_edit_user.add(delete)
keyboard_edit_user.add(remove_admin)

accept_user_del = types.InlineKeyboardButton(text = "ACCEPT", callback_data = "accept_user_del")

keyboard_accept_del = types.InlineKeyboardMarkup()
keyboard_accept_del.add(accept_user_del)

delete_product = types.InlineKeyboardButton(text='DELETE PRODUCT', callback_data = "delete_product")

del_product_keyboard = types.InlineKeyboardMarkup()
del_product_keyboard.add(delete_product)

keyboard_order = types.InlineKeyboardMarkup()
accept_order = types.InlineKeyboardButton(text = 'ACCEPT', callback_data = "accept_order")
delete_order = types.InlineKeyboardButton(text = 'DELETE', callback_data = "delete_order")
keyboard_order.add(accept_order)
keyboard_order.add(delete_order)
