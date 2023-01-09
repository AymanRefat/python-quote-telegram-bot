from bot.settings import bot 
from telebot import types 
from bot.views import texts 
import bot.views.keyboards as kb 


@bot.message_handler(commands=['start','help'])
def start(message:types.Message):
		bot.send_message(chat_id=message.chat.id,
										text=texts.generate_start_text(message.from_user.first_name)
										,reply_markup=kb.start_keyboard)
