from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, year_released, genre, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.year_released, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

