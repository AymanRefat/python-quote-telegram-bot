from telebot import types
from enum import Enum

class CallBackData(Enum):
		random_quote = "random_quote"
		today_quote = "today_quote"









quote_keyboard = types.InlineKeyboardMarkup(row_width=2)
random_quote = types.InlineKeyboardButton("Random Quote",callback_data=CallBackData.random_quote.value)
today_quote =  types.InlineKeyboardButton("Today Quote",callback_data=CallBackData.today_quote.value)
quote_keyboard.add(random_quote,today_quote)
