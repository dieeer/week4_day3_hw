from db.run_sql import run_sql

from models.book import Book
from models.author import Author 


def save(author):
    sql = "INSERT INTO authors (author_name, year_born, home_country) VALUES (%s, %s, %s) RETURNING *"
    values = [author.author_name, author.year_born, author.home_country]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def books(author):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['author_id'], row['year_released'], row['genre'])
        books.append(book)
    return books


