from telebot import types
from bot.settings import MY_TELEGRAM_LINK


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
