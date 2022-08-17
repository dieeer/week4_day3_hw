from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/', methods = ['GET'])
def books():
    books_list = book_repository.select_all()
    return render_template('index.html', all_books = books_list)