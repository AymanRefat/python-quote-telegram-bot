from telebot import types
from app.settings import MY_TELEGRAM_LINK
from enum import Enum

class CallBackData(Enum):
		random_quote = "random_quote"
		today_quote = "today_quote"







start_keyboard = types.InlineKeyboardMarkup(row_width=3)
owner = types.InlineKeyboardButton("Message Owner",url=MY_TELEGRAM_LINK,)
share = types.InlineKeyboardButton("Share me",
	switch_inline_query="I am Productive Bot Designed with ♥ by @AymanRefat1 , I will Help You be More Productive and Solve your Problems")
start_keyboard.row(owner,share)


quote_keyboard = types.InlineKeyboardMarkup(row_width=2)
random_quote = types.InlineKeyboardButton("Random Quote",callback_data=CallBackData.random_quote.value)
today_quote =  types.InlineKeyboardButton("Today Quote",callback_data=CallBackData.today_quote.value)
quote_keyboard.add(random_quote,today_quote)
