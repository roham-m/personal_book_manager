from books import show_book, save_book, load_book
from dotenv import load_dotenv
import os



name = input("Hello, please enter your name: ")

book_list = load_book()

print(f"Welcome {name} to the Personal Book Manager!")


admin_mode = input("do you want to enter admin mode (yes/no)?   ")

if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("admin_pass"):
        print("admin mode activated")

    else:
        print("wrong password!!!")


count = int(input("How many books do you want to add? : "))

for i in range(count):
    book = input("Enter a book name: ")
    book_list.append(book)

show_book(book_list)
save_book(book_list)