lass Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def display(self):
        print(f"Patron: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")

patron1 = Patron("Alice")
patron1.display()
