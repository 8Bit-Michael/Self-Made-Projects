# These just import some colors to make the output look more visually appealing:
from colorama import init, Fore
init(autoreset=True)
class Book:
    def __init__(self, title, author, is_borrowed): # This just sets up a book with a 
        self.title = title # title, author, and whether it is borrowed or not.
        self.author = author
        self.is_borrowed = is_borrowed
        
    def __str__(self): 
        # This tells the user what books they've borrowed in a readable format.
        # It's not too complicated, it just adds colors to the output in one line
        # instead of multiple lines:
        status = f"{Fore.RED}Borrowed." if self.is_borrowed else f"{Fore.GREEN}Available."
        return f"'{self.title}' by {self.author} - {status}"
        
class User:
    def __init__(self, name, borrowed_books): # This just sets up the user's name and borrowed books.
        self.name = name
        self.borrowed_books = borrowed_books

    def __str__(self): # This returns a string with the user's name and borrowed books
        if self.borrowed_books: # once activated.
            titles = [book.title for book in self.borrowed_books]
            return f"{self.name} has borrowed: {', '.join(titles)}"
        else:
            return (f"{self.name} has no borrowed books.")
        
# This is just a list of books that are available in the library, which you
# can modify to your liking.
my_books = [
    Book("Harry Potter And The Sorcerer's Stone", "J.K. Rowling", False),
    Book("The Hobbit", "J.R.R. Tolkien", False),
    # The true doesn't mean that the book is available, it actually means that the book is borrowed.
    Book("The Lord of The Rings", "J.R.R. Tolkien", True),
]
# Line 36 to 46 just gathers the user's input and checks if the input is valid or not.
user_name = input("Please enter your name: ").strip()
if any(char.isdigit() for char in user_name):
    print(Fore.RED + "Names can't contain numbers.")
    exit()
user_input = input("What books would you like? Enter the titles separated by commas: ")

requested_titles = user_input.replace(".", "").strip().split(",")
borrowed_books_list = []
# The validation part ends here.
# This part compares what the user wants to borrow with the books available in the library.
# If the book is available, they can borrow it, otherwise it will print an error message.
for title in requested_titles:
    cleaned_title = title.strip()
    for book in my_books:
        if cleaned_title.lower() == book.title.lower():
            if not book.is_borrowed:
                book.is_borrowed = True
                borrowed_books_list.append(book)
            else:
                print(Fore.YELLOW + f"'{book.title}' is already borrowed.")
            break
    else:
        print(Fore.RED + f"'{cleaned_title}' not found in library.")
# This sets up the user's profile in a way, with their name and list of borrowed books.
user = User(user_name, borrowed_books_list)

# The \n just adds an indent in the output, so it's not as complicated as it looks.
# Also, it shows the library's status, including the books that are borrowed and available.
print("\nLibrary Status:")
# This just compares:
for book in my_books:
    print(book)
# This just prints the user's status when it comes to the books they've borrowed.
print("\nUser Status:")
print(user)

    
