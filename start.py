from bot import importing, settings
from helpers import functions as f

logger = f.get_logger()


def start() -> None:
    importing.import_bot()
    logger.info("Bot is Installed")
    f.import_all_features(settings.INSTALLED_FEATURES)
    settings.bot.infinity_polling()


if __name__ == "__main__":
    start()
