from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books', methods = ['GET'])
def books():
    books_list = book_repository.select_all()
    return render_template('index.html', all_books = books_list)

@books_blueprint.route('/books/new', methods = ['GET'])
def new_book():
    authors_list = author_repository.select_all()
    return render_template('books/new.html', all_authors = authors_list)

@books_blueprint.route('/books', methods = ['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    year_released = request.form['year_released']
    genre = request.form['genre']
    author = author_repository.select(author_id)
    # assumes there is matching user
    book = Book(title, author, year_released, genre)
    book_repository.save(book)
    return redirect('/books')
    