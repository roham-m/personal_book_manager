name = input("Hello, please enter your name: ")

book_list = []

print(f"Welcome {name} to the Personal Book Manager!")

count = int(input("How many books do you want to add? : "))

for i in range(count):
    book = input("Enter a book name: ")
    book_list.append(book)

print(f"\n{name}, your favorite books are:")

for book in book_list:
    print(book)