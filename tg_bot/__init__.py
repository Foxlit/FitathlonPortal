import telebot

myBotToken = ""

bot = telebot.TeleBot(myBotToken)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Приветули")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "не понял")


bot.infinity_polling()
