from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.db import add_books_db


class AddBooks(StatesGroup):
    name = State()
    book_id= State()
    author= State()
    genre= State() 


router_addbooks = Router()


@router_addbooks.message(Command('add_book'))
async def add_book_fsm(message: Message, state: FSMContext):
    await message.answer('Введите номер книги:')
    await state.set_state(AddBooks.book_id)


@router_addbooks.message(AddBooks.book_id)
async def get_number_fsm(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.answer("Введите номер книги только числом!")
        return
    
    await state.update_data(book_id=int(message.text))
    await message.answer('Введите название книги:')
    await state.set_state(AddBooks.name)

@router_addbooks.message(AddBooks.name)
async def add_name_fsm(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите автора книги:')
    await state.set_state(AddBooks.author)

@router_addbooks.message(AddBooks.author)
async def add_author_fsm(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer('Введите жанр книги')
    await state.set_state(AddBooks.genre)


@router_addbooks.message(AddBooks.genre)
async def add_genre_fsm(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)

    data = await state.get_data()

    await message.answer(
                        "📚 Книга добавлена!\n"
                        f"Номер: {data['book_id']}\n"
                        f"Название: {data['name']}\n"
                        f"Автор: {data['author']}\n"
                        f"Жанр: {data['genre']}")


    await add_books_db(book_id=data['book_id'], name=data['name'], author=data['author'], genre=data['genre'])
    await state.clear()

    


