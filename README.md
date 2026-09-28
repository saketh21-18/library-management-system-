# 📚 Library Management System

A terminal program to manage a small library: add books, view them, issue and return them, and search by title or author. Data is saved in a JSON file.

## Concepts Used
OOP (classes) • Lists • Dictionaries • File handling

## Requirements
- Python 3.7+
- No external libraries (uses built-in `json` and `os`)

## How to Run
```bash
python library_management.py
```
On Mac/Linux use `python3`.

## Menu
```
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Search Book
6. Exit (saves data)
```

## How It Works
- The `Library` class keeps all books in a **list of dictionaries**:
```python
  {"id": "1", "title": "Python Basics", "author": "Guido", "issued_to": None}
```
- `issued_to` is `None` when the book is available, or the student's name when it is issued.
- Issuing checks that the book exists and isn't already issued. Returning checks that it was actually issued.
- Search is case-insensitive and matches part of a title or author.
- Data loads from `library.json` on startup and saves on exit.

## Example
```
Enter choice: 1
Book ID: 1
Title: Python Basics
Author: Guido
Book added.

Enter choice: 3
Book ID: 1
Student name: Anita
Book issued.
```

## Tips
- Use a unique Book ID for every book.
- Always choose **6. Exit** so changes are saved.
- Try searching with just part of a name, like `pyth`.
- To reset the library, delete `library.json`.

## Ideas to Extend
- Add issue dates, due dates and fines
- Limit how many books one student can borrow
- Add a "view issued books only" option
