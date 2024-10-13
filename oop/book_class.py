class Book:
    def __init__(self, title, author, year):
        self.title = title        # The title of the book.
        self.author = author         # The author of the book
        self.year = int(year)          # The publication year of the book.

    def __del__(self):
        self.title   # Deleting title of the book.
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

