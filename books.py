import json

def show_book(book_list):
    for book in book_list:
        print(book)

def load_book():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_book(book_list):
    with open("books.json", "w") as file:
        json.dump(book_list, file, indent=2)