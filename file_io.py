import json


def read_books(database_file):
    """Read all Json data from bookstore database file."""
    with open(database_file, 'r') as f:
        book_list = f.read()
    return book_list


def save_books(book_list, database_file):
    """Update book data in bookstore database file."""
    book_dict = json.dumps(book_list, indent=4)
    with open(database_file, 'w') as f:
        f.write(book_dict)
