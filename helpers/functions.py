from telebot.types import BotCommand
from logging import Logger


def get_commands_from_feature(
    feature_name: str, target_file: str = "settings"
) -> list[BotCommand]:
    """get the commands from someFeature like ``from feature.setttings import COMMANDS``
    - ``target_file`` is the file that contains commands by default it's called ``settings``
    """

    return __import__(f"{feature_name}.{target_file}", fromlist=[None]).COMMANDS


def get_all_commands(installed_features: list[str]) -> list[BotCommand]:
    """get all the commands in all Features by importing every command list from each feature"""

    commands = []

    for feature_name in installed_features:
        cmds = get_commands_from_feature(feature_name)
        for command in cmds:
            commands.append(command)

    return commands


def import_feature(
    feature_name: str,
    parent_folder: str = "views",
    files: list[str] = ["commands", "queries"],
) -> None:
    """it's Trying to import the files those will make the bot work"""

    # Check if the parent_folder exists or right
    parent = (
        True if parent_folder is not None and parent_folder.strip() != "" else False
    )

    if parent:
        for file in files:
            __import__(f"{feature_name}.{parent_folder}.{file}", fromlist=[None])

    else:
        for file in files:
            __import__(f"{feature_name}.{file}", fromlist=[None])


def get_logger() -> Logger:
    from bot.logger import logger

    return logger


def import_all_features(installed_features: list[str], logging: bool = True) -> None:
    """for Each Feature it's Trying to import"""

    for feature_name in installed_features:
        import_feature(feature_name)
        if logging:
            get_logger().info(f"Feature {feature_name} is installed")
