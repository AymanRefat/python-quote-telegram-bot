from telebot import types
from helpers import BaseQuery
from .commands import CallBackData
from quotes.api import quotes


quote_api = quotes.QuotesAPI()


class RandomQuoteQuery(BaseQuery):
    def dispather(self, call) -> bool:
        return call.data == CallBackData.random_quote.value

    def query(self, query: types.CallbackQuery):
        self.bot.send_message(
            chat_id=query.message.chat.id, text=quote_api.get_random_quote()
        )


class TodayQuoteQuery(BaseQuery):
    def dispather(self, call) -> bool:
        return call.data == CallBackData.today_quote.value

    def query(self, query: types.CallbackQuery):
        self.bot.send_message(
            chat_id=query.message.chat.id, text=quote_api.get_today_quote()
        )
