from telebot import TeleBot

TOKEN = "8739585308:AAGduAC1pBGdR-D9MUH25qQQRH5SGdENub0"
ADMIN_ID = 8191930658

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Salom! Xabaringizni yuboring.")

@bot.message_handler(func=lambda m: True)
def forward(msg):
    if msg.chat.id != ADMIN_ID:
        bot.forward_message(ADMIN_ID,