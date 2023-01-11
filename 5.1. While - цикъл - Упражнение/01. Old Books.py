fave_book = input()
shelf_books = input()
counter = 0

while shelf_books != "No More Books":
    if shelf_books == fave_book:
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    shelf_books = input()

if shelf_books == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {counter} books.")
