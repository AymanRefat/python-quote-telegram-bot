def import_bot() -> None:
    """Plug the bot Commands and Queries by Importing their Files"""
    from bot import settings
    from bot.views import commands, keyboards
