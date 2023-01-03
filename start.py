from app.bot import bot 
from app.utils import set_commands , set_queries



def start()->None:
	set_commands()
	set_queries()
	bot.infinity_polling()  





if __name__ == "__main__":
	start()

