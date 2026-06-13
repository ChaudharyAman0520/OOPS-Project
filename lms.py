class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__available = True

    def is_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def __str__(self):
        status = "Available" if self.__available else "Issued"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def get_borrow_limit(self):
        return 0

    def borrow_book(self, book):
        if not book.is_available():
            print("Book is already issued.")
            return

        if len(self.borrowed_books) >= self.get_borrow_limit():
            print("Borrow limit reached.")
            return

        self.borrowed_books.append(book)
        book.set_available(False)
        print(f"'{book.title}' borrowed successfully.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_available(True)
            print(f"'{book.title}' returned successfully.")
        else:
            print("You have not borrowed this book.")


class Student(Member):
    def get_borrow_limit(self):
        return 2


class Librarian(Member):
    def get_borrow_limit(self):
        return 5

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available():
                    print("Cannot remove an issued book.")
                    return
                self.books.remove(book)
                print("Book removed successfully.")
                return

        print("Book not found.")

    def display_books(self):
        print("\n========== BOOK LIST ==========")
        for book in self.books:
            print(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

library = Library()
library.add_book(Book(1, "Python Programming", "Guido"))
library.add_book(Book(2, "Java Fundamentals", "James Gosling"))
library.add_book(Book(3, "Data Structures", "Mark Allen"))
library.add_book(Book(4, "Operating Systems", "Galvin"))
library.add_book(Book(5, "Computer Networks", "Kurose"))

print("===== LIBRARY MANAGEMENT SYSTEM =====")
print("1. Student")
print("2. Librarian")

role = int(input("Select Role: "))
name = input("Enter Name: ")

if role == 1:
    user = Student(1, name)

    while True:
        print("\n===== STUDENT MENU =====")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Borrowed Books")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            library.display_books()

        elif choice == 2:
            library.display_books()
            book_id = int(input("Enter Book ID: "))
            book = library.find_book(book_id)

            if book:
                user.borrow_book(book)
            else:
                print("Book not found.")

        elif choice == 3:
            book_id = int(input("Enter Book ID to return: "))
            book = library.find_book(book_id)

            if book:
                user.return_book(book)
            else:
                print("Book not found.")

        elif choice == 4:
            print("\n===== BORROWED BOOKS =====")
            if not user.borrowed_books:
                print("No books borrowed.")
            else:
                for book in user.borrowed_books:
                    print(book)

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid choice.")

elif role == 2:
    user = Librarian(1, name)

    while True:
        print("\n===== LIBRARIAN MENU =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View Borrowed Books")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            library.display_books()

        elif choice == 2:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")

            new_book = Book(book_id, title, author)
            user.add_book(library, new_book)

        elif choice == 3:
            book_id = int(input("Enter Book ID to remove: "))
            user.remove_book(library, book_id)

        elif choice == 4:
            library.display_books()
            book_id = int(input("Enter Book ID: "))

            book = library.find_book(book_id)

            if book:
                user.borrow_book(book)
            else:
                print("Book not found.")

        elif choice == 5:
            book_id = int(input("Enter Book ID to return: "))

            book = library.find_book(book_id)

            if book:
                user.return_book(book)
            else:
                print("Book not found.")

        elif choice == 6:
            print("\n===== BORROWED BOOKS =====")
            if not user.borrowed_books:
                print("No books borrowed.")
            else:
                for book in user.borrowed_books:
                    print(book)

        elif choice == 7:
            print("Thank You!")
            break

        else:
            print("Invalid choice.")

else:
    print("Invalid role selected.")