class Book:

  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_borrowed = False

  def borrow(self):
    if not self.is_borrowed:
      self.is_borrowed = True
      return True
    return False

  def return_book(self):
    if self.is_borrowed:
      self.is_borrowed = False
      return True
    return False

  def __str__(self):
    status = "Borrowed" if self.is_borrowed else "Available"
    return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"


class Patron:

  def __init__(self, name, patron_id):
    self.name = name
    self.patron_id = patron_id
    self.borrowed_books = []

  def borrow_book(self, book):
    if book.borrow():
      self.borrowed_books.append(book)
      print(f"Success: {self.name} borrowed '{book.title}'.")
    else:
      print(f"Error: '{book.title}' is already borrowed.")

  def return_book(self, book):
    if book in self.borrowed_books and book.return_book():
      self.borrowed_books.remove(book)
      print(f"Success: {self.name} returned '{book.title}'.")
    else:
      print(f"Error: {self.name} does not have '{book.title}'.")

  def __str__(self):
    return f"Patron: {self.name} (ID: {self.patron_id})"


class Library:

  def __init__(self):
    self.books = []
    self.patrons = []

  def add_book(self, book):
    self.books.append(book)
    print(f"Added book: '{book.title}'")

  def register_patron(self, patron):
    self.patrons.append(patron)
    print(f"Registered patron: {patron.name}")

  def display_books(self):
    print("\n--- Library Books ---")
    for book in self.books:
      print(book)

  def display_patrons(self):
    print("\n--- Registered Patrons ---")
    for patron in self.patrons:
      print(patron)


# --- Main Program Execution ---
if __name__ == "__main__":
  # 1. Create Library Instance
  city_library = Library()

  # 2. Add Books
  book1 = Book("1984", "George Orwell", "9780451524935")
  book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
  book3 = Book(
      "The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"
  )

  city_library.add_book(book1)
  city_library.add_book(book2)
  city_library.add_book(book3)

  # 3. Register Patrons
  patron1 = Patron("Alice", "P101")
  patron2 = Patron("Bob", "P102")

  city_library.register_patron(patron1)
  city_library.register_patron(patron2)

  # 4. Display Initial Status
  city_library.display_books()

  # 5. Borrow Books
  print("\n--- Borrowing Operations ---")
  patron1.borrow_book(book1)
  patron2.borrow_book(book1)  # Trying to borrow an already borrowed book

  # 6. Display Status After Borrowing
  city_library.display_books()

  # 7. Return Books
  print("\n--- Returning Operations ---")
  patron1.return_book(book1)

  # 8. Display Final Status
  city_library.display_books()