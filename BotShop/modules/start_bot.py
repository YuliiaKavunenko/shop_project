import telebot
import sqlite3
from telebot import types
import modules.data_base as m_data
import modules.create_keyboard as m_keyboard

@m_data.bot.message_handler(commands = ["start"])
def bot_start(message):
    m_data.bot.send_message(
        chat_id = message.chat.id,
        text = "Привіт, користувач.",
        reply_markup = m_keyboard.keyboard_menu
        )
    


