from dotenv import load_dotenv
from helpers import BaseBotManager
from quotes.feature import QuotesFeature
from .commands import StartCommand

load_dotenv()


class BotManager(BaseBotManager):
    commands = [StartCommand]
    features = [QuotesFeature]

    def start_bot(self) -> None:
        self.register_features()
        self.set_bot_commands()
        self.bot.infinity_polling()


manager = BotManager()
