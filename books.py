import json

def show_book(book_list):
    print("\n----- Your Books -----")

    for book in book_list:
        print(f"Book Name: {book['name']}")
        print(f"Priority: {book['priority']}")
        print("----------------------")

    print(f"Total number of books saved: {len(book_list)}")
    print("----------------------")

def load_book():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)

            return books

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_book(book_list):
    with open("books.json", "w") as file:
        json.dump(book_list, file, indent=2)