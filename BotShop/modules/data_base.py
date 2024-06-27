import telebot, sqlite3, os

xl_path = os.path.abspath(__file__+"/../../../project/products_shop.xlsx")
path = os.path.abspath(__file__ + "/../../../project/data.db")

TOKEN = "7471892975:AAGq2mgH5G2G-GHEbL8rq5auLVxO_-owXY0"
bot = telebot.TeleBot(TOKEN)

connection = sqlite3.connect(path, check_same_thread = False)
cursor = connection.cursor()


