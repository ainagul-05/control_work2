import aiosqlite
from config import path_db
from database.queries import  create_books_table,create_books_detaiil_table,insert_books,insert_books_detail ,get_books


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(create_books_table)
        await conn.execute(create_books_detaiil_table)
        await conn.commit()


async def add_books_db( book_id,name, author, genre ):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(insert_books, (book_id, name, author))
        await conn.execute(insert_books_detail, (book_id,genre))
        await conn.commit()


async def get_books_db():

 async with aiosqlite.connect(path_db) as conn:
    cursor = await conn.execute(get_books)
    books = await cursor.fetchall()
 return books



    




