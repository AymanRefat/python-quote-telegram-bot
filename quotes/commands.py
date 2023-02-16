from helpers import BaseCommand
from telebot import types
from enum import Enum


class CallBackData(Enum):
    random_quote = "random_quote"
    today_quote = "today_quote"


class QuoteCommand(BaseCommand):
    commands = ["quote", "quotes"]
    base_command = "quote"
    description = "Show all options for getting quotes"

    def command(self, message) -> None:
        self.bot.send_message(
            chat_id=message.chat.id,
            text="These are the Options for Quotes,Enjoy!",
            reply_markup=self.quote_keyboard(),
        )

    def quote_keyboard(self):
        quote_keyboard = types.InlineKeyboardMarkup(row_width=2)
        random_quote = types.InlineKeyboardButton(
            "Random Quote", callback_data=CallBackData.random_quote.value
        )
        today_quote = types.InlineKeyboardButton(
            "Today Quote", callback_data=CallBackData.today_quote.value
        )
        quote_keyboard.add(random_quote, today_quote)
        return quote_keyboard
