from db.run_sql import run_sql

from models.book import Book
from models.author import Author

def save(book):
    sql = "INSERT INTO books (title, author_name, year_released, genre) VALUES (%s %s %s %s) RETURNING *"
    values = [book.title, book.author_name, book.year_released, book.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book