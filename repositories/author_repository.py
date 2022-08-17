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

def select(id):
    author = None
    
    sql = 'SELECT * FROM authors WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        author = Author(result['author_name'],
                        result['year_born'], 
                        result['home_country'], 
                        result['id'])
    return author


def select_all():
    authors = []
    
    sql = 'SELECT * FROM authors'
    results = run_sql(sql)
    
    for row in results:
        author = Author(row['author_name'], row['year_born'], row['home_country'], row['id'])
        authors.append(author)
    return authors

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


