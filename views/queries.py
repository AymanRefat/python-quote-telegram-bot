from app.bot import bot
from telebot import types
from views import keyboards as kb
from api import quotes

quote_api = quotes.QuotesAPI()


@bot.callback_query_handler(
    func=lambda call: call.data == kb.CallBackData.random_quote.value
)
def send_random_quote(query: types.CallbackQuery):
    """Send Random Quote to the User"""
    bot.send_message(chat_id=query.message.chat.id, text=quote_api.get_random_quote())


@bot.callback_query_handler(
    func=lambda call: call.data == kb.CallBackData.today_quote.value
)
def send_today_quote(query: types.CallbackQuery):
    """Send the Today Quote to the User"""
    bot.send_message(chat_id=query.message.chat.id, text=quote_api.get_today_quote())
