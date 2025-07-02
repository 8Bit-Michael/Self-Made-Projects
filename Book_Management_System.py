from colorama import init, Fore
init(autoreset=True)

library = ['The Lord of The Rings', 'Harry Potter And The Chamber of Secrets', 
           'Harry Potter And The Prizoner of Azkaban', "Harry Potter And The Sorcorer's Stone"]
max_capacity = 5
book_count = 4

def add_book(book_title):
    global library, book_count, max_capacity

    if book_count == max_capacity:
        new_capacity = max_capacity * 2
        new_library = []

        for book in library:
            new_library.append(book)

        new_library.append(book_title)

        library = new_library
        book_count += 1
        max_capacity = new_capacity
    else:
        if book_count < len(library):
            library[book_count] = book_title
        else:
            library.append(book_title)
        book_count += 1
        
def display_books():
    print(", ".join(library[:book_count]))

add_book('Another book5')
display_books()
