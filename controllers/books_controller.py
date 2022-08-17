from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

