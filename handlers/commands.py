from aiogram import F , Router
from aiogram.filters import Command
from aiogram.types import Message
from config import bot
from database import db 



router_commands = Router() 

@router_commands.message(Command('start'))
async def  sratr_hundler(message: Message):
    await message.answer( text='Добро пожаловать в наш книжный магазин!')


@router_commands.message(Command("books")) 
async def books(message: Message):


    
    books = await db.get_books_db()

    if not books:

      await message.answer("📚 Каталог книг пока пуст.")
      return

    for book in books:
       await message.answer(
                f"📚 Книга\n\n"
                f"Номер: {book[0]}\n"
                f"Название: {book[1]}\n"
                f"Автор: {book[2]}\n"
                f"Жанр: {book[3]}"
    )
        