class Book("title, author"):
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived Classes
class EBook(Book):
    def __init__(self, title, author, file_size):
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = int(page_count)

# Composition
class Library(Book):
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.book = Book, EBook, PrintBook

    def list_books(self):
        self.book 

        