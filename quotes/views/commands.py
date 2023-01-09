from bot.settings import bot
from quotes.views import keyboards as kb


@bot.message_handler(commands=["quote"])
def quote(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="These are the Options for Quotes,Enjoy!",
        reply_markup=kb.quote_keyboard,
    )
