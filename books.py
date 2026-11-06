import json

def show_book(book_list):
    for book in book_list:
        print(f"Book: {book['name']} | Priority: {book['priority']}")

def load_book():
    try:
        with open("books.json", "r") as file:
            books = json.load(file)

            for book in books:
                if isinstance(book, str):
                    return []

            return books

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_book(book_list):
    with open("books.json", "w") as file:
        json.dump(book_list, file, indent=2)