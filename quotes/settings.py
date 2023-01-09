from telebot.types import BotCommand


COMMANDS: list[BotCommand] = [
    BotCommand(command="quote", description="Show all options for getting quotes"),
]
