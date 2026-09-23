create_books_table = """ CREATE TABLE IF NOT EXISTS books(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     book_id INTEGER NOT NULL,
     name TEXT NOT NULL,
     author TEXT
     ) """


create_books_detaiil_table = """
CREATE TABLE IF NOT EXISTS books_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    genre TEXT 
    )
    """

insert_books = 'INSERT INTO books (book_id, name, author) VALUES (?, ?, ?)'
insert_books_detail = 'INSERT INTO books_detail (book_id,genre) VALUES (?, ?)'


get_books = """
     SELECT books.book_id,books.name,books.author,books_detail.genre
     FROM books
     INNER JOIN books_detail
     ON books.book_id = books_detail.book_id 
"""
