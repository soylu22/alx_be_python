# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: initializes book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: prints message when object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for readable output"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation for recreating the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
