book_searched = input()
book_from_shelf = input()
books_looked = 0
while book_from_shelf != book_searched:
    if book_from_shelf == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_looked} books.")
        break
    books_looked += 1
    book_from_shelf = input()
else:
    print(f"You checked {books_looked} books and found it.")