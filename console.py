import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# book_repository.delete_all()
# author_repository.delete_all()

book1 = Book("Dune", 1965, "sci-fi", author1)

author1 = Author("Frank Herbert", 1920, "United States")

pdb.set_trace()