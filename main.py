import json
import os

FILE_NAME = "library.json"


class Library:
    def __init__(self):
        self.books = []  # list of dictionaries
        self.load()

    def load(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                self.books = json.load(f)

    def save(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, book_id, title, author):
        for book in self.books:
            if book["id"] == book_id:
                print("Book ID already exists.")
                return
        self.books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "issued_to": None
        })
        print("Book added.")

    def view_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            status = "Available" if book["issued_to"] is None else f"Issued to {book['issued_to']}"
            print(f"[{book['id']}] {book['title']} by {book['author']} - {status}")

    def issue_book(self, book_id, student_name):
        for book in self.books:
            if book["id"] == book_id:
                if book["issued_to"] is None:
                    book["issued_to"] = student_name
                    print("Book issued.")
                else:
                    print("Book already issued.")
                return
        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["issued_to"] is not None:
                    book["issued_to"] = None
                    print("Book returned.")
                else:
                    print("This book was not issued.")
                return
        print("Book not found.")

    def search(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                print(f"[{book['id']}] {book['title']} by {book['author']}")
                found = True
        if not found:
            print("No matching books.")


def main():
    lib = Library()
    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            lib.add_book(input("Book ID: "), input("Title: "), input("Author: "))
        elif choice == "2":
            lib.view_books()
        elif choice == "3":
            lib.issue_book(input("Book ID: "), input("Student name: "))
        elif choice == "4":
            lib.return_book(input("Book ID: "))
        elif choice == "5":
            lib.search(input("Search keyword: "))
        elif choice == "6":
            lib.save()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
