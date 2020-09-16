import os
import re
import console_io
import file_io
import sys
import json


def main():
    """ Main Bookstore application """
    book_list = []
    if len(sys.argv) != 2:
        print(" invalid argument.")
        exit(0)

    database_file = sys.argv[1]

    if not os.path.exists(database_file):
        print("The bookstore database does not exists")
    else:
        books = file_io.read_books(database_file)
        book_list = json.loads(books)
    user_input = ""
    while user_input != "q":
        user_input = input(
            "Enter an action - Add (a),Delete (d),View Summary (s),Search by Title(t), "
            "Search by Author (u),Search by Keyword(k), Quit(q):")

        try:
            if user_input == "a":
                title, author, isbn, year, desc = console_io.get_book_details()

                book = {"title": title, "author": author, "isbn": isbn, "year": year, "desc": desc}

                book_list.append(book)
                file_io.save_books(book_list, database_file)

            elif user_input == "d":
                isbn = console_io.get_isbn()

                # Make sure you don't remove items from a list
                # you are iterating through
                books_deleted = 0
                for book in book_list[:]:
                    if book['isbn'] == isbn:
                        book_list.remove(book)
                        books_deleted += 1

                if books_deleted > 0:
                    file_io.save_books(book_list, database_file)
                    print("Deleted %d books" % books_deleted)
                else:
                    print("No matching books found")

            elif user_input == "s":
                console_io.display_book_summaries(book_list)

            elif user_input == "t":
                search_str = console_io.get_title()

                filtered_books = []
                for book in book_list:
                    if re.search(search_str, book["title"], re.IGNORECASE) is not None:
                        filtered_books.append(book)
                console_io.display_book_summaries(filtered_books)

            elif user_input == "u":
                search_str = console_io.get_author()

                filtered_books = []
                for book in book_list:
                    if re.search(search_str, book["author"], re.IGNORECASE) is not None:
                        filtered_books.append(book)
                console_io.display_book_summaries(filtered_books)

            elif user_input == 'k':
                search_str = console_io.get_keyword()

                filtered_books = []
                for book in book_list:
                    title_search = re.search(search_str, book["title"])
                    desc_search = re.search(search_str, book["desc"])
                    if title_search is not None or desc_search is not None:
                        filtered_books.append(book)
                console_io.display_book_summaries(filtered_books)

            else:
                print("Invalid action")

        except ValueError as v_err:
            print("Value Error: %s" % str(v_err))
        except TypeError as t_err:
            print("Type Error: %s" % str(t_err))


if __name__ == "__main__":
    main()
