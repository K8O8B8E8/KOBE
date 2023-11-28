'''import telebot

token = '6971822450:AAGaIYzs1L4BaCppLgaOouiAbO_5sCBx0qM'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    bot.send_message(message.chat.id, "Напишите логин от аккаунта")
    bot.register_next_step_handler(message, add_user1)


bot.infinity_polling()

'''