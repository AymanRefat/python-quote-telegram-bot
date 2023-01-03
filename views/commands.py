from app.bot import bot 
from telebot import types
from views import keyboards as kb 
from views import texts 


@bot.message_handler(commands=['start','help'])
def start(message:types.Message):
		bot.send_message(chat_id=message.chat.id,
										text=texts.start_text(message.from_user.first_name)
										,reply_markup=kb.start_keyboard)

@bot.message_handler(commands=['quote'])
def quote(message):
		bot.send_message(chat_id = message.chat.id,
					text="These are the Options for Quotes,Enjoy!",reply_markup=kb.quote_keyboard)
