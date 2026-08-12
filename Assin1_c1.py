class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        
    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

my_book = Book("The Great Gatsby","F. Scott")
my_book.display()
