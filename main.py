from books import show_book, save_book, load_book
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Hello, please enter your name: ")

book_list = load_book()

if book_list is None:
    book_list = []

print(f"Welcome {name} to the Personal Book Manager!")

admin_mode = input("Do you want to enter admin mode (yes/no)? ").lower()

if admin_mode == "yes":
    admin_password = input("Enter admin password: ")

    if admin_password == os.getenv("admin_pass"):
        print("Admin mode activated")
    else:
        print("Wrong password!!!")

count = int(input("How many books do you want to add? : "))

for i in range(count):
    book = input("Enter a book name: ")

    priority = input("Enter priority (low/medium/high): ").lower()

    while priority not in ["low", "medium", "high"]:
        print("Invalid priority!")
        priority = input("Enter priority (low/medium/high): ").lower()

    book_list.append({
        "name": book,
        "priority": priority
    })

show_book(book_list)
save_book(book_list)