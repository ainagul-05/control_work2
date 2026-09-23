from aiogram import  Bot, Dispatcher
from decouple import config



token_bot = config("TOKEN")


bot = Bot(token=token_bot)
dp = Dispatcher()

path_db = 'database/bot.db'


