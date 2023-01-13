from telebot import types
import os
from helpers.classes.command import BaseCommand

MY_TELEGRAM_LINK = os.getenv("MY_TELEGRAM_LINK", "https://t.me/AymanRefat1")


class StartCommand(BaseCommand):
    commands = ["start", "help"]
    base_command = "start"
    description = "Start the bot"

    def command(self, message: types.Message) -> None:
        self.bot.send_message(
            chat_id=message.chat.id,
            text=self.get_start_message(message.from_user.first_name),
            reply_markup=self.get_inlinemarkup(),
        )

    def get_start_message(self, name) -> str:
        """Generate the Welcome text to the user"""
        start_text = f"""Hi {name} , I am your AI assistant🤖 and am here for Helping you message me whenever you need 😉! ,There are some things I can help you with."""
        return start_text

    def get_inlinemarkup(self) -> types.InlineKeyboardMarkup:
        start_keyboard = types.InlineKeyboardMarkup(row_width=3)
        owner = types.InlineKeyboardButton(
            "Message Owner",
            url=MY_TELEGRAM_LINK,
        )
        share = types.InlineKeyboardButton(
            "Share me",
            switch_inline_query="\nI am Productive Bot Designed with ♥ by @AymanRefat1 , I will Help You be More Productive and Solve your Problems",
        )
        start_keyboard.row(owner, share)
        return start_keyboard
