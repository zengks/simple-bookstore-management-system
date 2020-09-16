import re
import datetime


def get_book_details():
    """Get and validates book details of a new book to be added to the bookstore database"""
    title_input = input("Please enter new book's title: ")
    if not re.search("[A-Za-z0-9\s]+", title_input):
        raise ValueError("Title is not valid")

    author = input("Please enter new book's author: ")
    if not re.search("[A-Za-z\s]+", author):
        raise ValueError("Author is not valid")

    isbn = input("Please enter new book's ISBN: ")
    if not re.search("^[0-9]+$", isbn):
        raise TypeError("ISBN must be digits only")
    elif not re.search("^[0-9]{4,20}$", isbn):
        raise ValueError("ISBN must be 4 to 20 digits")

    year = input("Please enter new book's year published: ")
    if not re.search(r"^[0-9]+$", year):
        raise TypeError("Year must be digits only")
    elif not re.search(r"^[0-9]{4}$", year):
        raise ValueError("Year must be four digits")
    elif not 1900 <= int(year) <= int(current_year()):
        raise ValueError("Year must be between 1900 and current year")

    description = input("Please enter new book's description: ")
    if not re.search(r"^.{1,256}$", description):
        raise ValueError("Description cannot exceed 256 characters in length")

    return title_input, author, isbn, year, description


def display_book_summaries(book_list):
    """Display all book details on a new line."""
    if len(book_list) == 0:
        print("Nothing to show!")
    else:
        for book in book_list:
            print("Title: %s, Author: %s, ISBN: %d, Year: %d, Description: %s\n" %
                  (book["title"], book["author"], int(book["isbn"]), int(book["year"]), book["desc"][0:30]))


def current_year():
    """This method uses methods from datetime library to generate current year.

    :return: year of current time.
    """
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    return year


def get_isbn():
    """Get and validates ISBN of the book from user to search for."""
    isbn = input("Please enter the ISBN of book you want to delete: ")
    if not re.search("^[0-9]+$", isbn):
        raise TypeError("ISBN must be digits only")
    elif not re.search("^[0-9]{4,20}$", isbn):
        raise ValueError("ISBN must be 4 to 20 digits")
    return isbn


def get_title():
    """Get and validates title of book from user to search for."""
    title = input("Please enter the title of book you are searching for: ")
    if not re.search("[A-Za-z0-9\s]+", title):
        raise ValueError("Title is not valid")
    return title


def get_author():
    """Get and validates author of book from user to search for."""
    author = input("Please enter the author of book you are searching for: ")
    if not re.search("[A-Za-z\s]+", author):
        raise ValueError("Author is not valid")
    return author


def get_keyword():
    """Get keyword of information on book that user wants to search for."""
    keyword = input("Please enter the keyword to search for: ")
    if not re.search("^.{1,20}$", keyword):
        raise ValueError("Keyword cannot exceed 20 characters in length")
    return keyword
