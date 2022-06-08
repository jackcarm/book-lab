import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("John", "Smith")
author_repository.save(author_1)

author_2 = Author("Jane", "Doe")
author_repository.save(author_2)


book_1 = Book("The Happening", author_1)
book_repository.save(book_1)

book_repository.select_all

pdb.set_trace()
