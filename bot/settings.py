import telebot, os
from dotenv import load_dotenv
from telebot.types import BotCommand

from helpers import functions as f

load_dotenv()

TOKEN = os.getenv("TOKEN")
MY_TELEGRAM_LINK = os.getenv("MY_TELEGRAM_LINK")
INSTALLED_FEATURES = ["quotes"]


bot = telebot.TeleBot(TOKEN)


bot.set_my_commands(
    [
        BotCommand(command="start", description="Start the bot"),
    ]
    + f.get_all_commands(INSTALLED_FEATURES)
)
