"""
Program 5(b) - Lab Exercise 2 – Library management system
Source: Python Lab Report
"""

# Lab Exercise 2: Library management system

class Book:
    def __init__(self, book_id, title, author):
        self.book_id, self.title, self.author = book_id, title, author
        self.available = True
    def __str__(self):
        status = "Available" if self.available else "Issued"
        return (f"{self.book_id:<4}{self.title:<26}"
                f"{self.author:<14}{status}")

class Library:
    def __init__(self):
        self.books = []
    def find(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    def issue(self, book_id):
        book = self.find(book_id)
        if book is None or not book.available:
            print("Book not found or already issued.")
        else:
            book.available = False
            print(f"Issued: {book.title}")
    def return_book(self, book_id):
        book = self.find(book_id)
        if book is None or book.available:
            print("Invalid return request.")
        else:
            book.available = True
            print(f"Returned: {book.title}")

lib = Library()
lib.books.append(Book("B1", "Learning Python", "Mark Lutz"))
lib.books.append(Book("B2", "Think Python", "Allen Downey"))
lib.books.append(Book("B3", "Python for Data Analysis", "Wes McKinney"))

while True:
    print("\n1.Display  2.Issue  3.Return  4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        for b in lib.books:
            print(b)
    elif choice == "2":
        lib.issue(input("Enter book ID to issue: "))
    elif choice == "3":
        lib.return_book(input("Enter book ID to return: "))
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
