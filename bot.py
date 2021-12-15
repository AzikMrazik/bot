import telebot

bot = telebot.TeleBot(5097465180:AAFezAkYbiVyBPwL1ujdcYG2PuJh8iYYpzs) 


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
