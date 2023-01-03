import telebot 
from app.settings import TOKEN  
from telebot.types import BotCommand
bot = telebot.TeleBot(TOKEN)


bot.set_my_commands(
      [BotCommand(command='start',description="Start the bot"),
      BotCommand(command='quote',description="Show all options for getting quotes"),
      ]
)
