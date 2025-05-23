# "pip install colorama" has to been installed using the terminal.
from colorama import init, Fore
init(autoreset=True)
# The input part of the code:
def first_check():
    global x
    first_input = input("Welcome to my evaluating app! Please enter your first number: ")
    try:
        x = int(first_input)
        second_check()
    except ValueError:
        print(f"'{first_input}' is not a valid number, please try again.\n")
        first_check()

def second_check():
    global y
    second_input = input("Please enter your second number: ")
    try:
        y = int(second_input)
        less_more_equal()
    except ValueError:
        print(f"'{second_input}' is not a valid number, please try again.\n")
        second_check()

# The math part of the code:

def less_more_equal():
    if x > y:
        print(Fore.GREEN + f"{x} is more than {y}!")
        # The loop part:
        keep_going = input("Would you like to continue? Type yes or no: ")
        if keep_going.lower().strip() == 'yes':
            first_check()
        elif keep_going.lower().strip() == 'no':
            print("Okay, thanks for using my app.")
        else:
            print("Your input is invalid, please try again.")
            less_more_equal()
    elif x == y:
        print(Fore.GREEN + f"{x} and {y} are equal!")
        # The loop part:
        keep_going = input("Would you like to continue? Type yes or no: ")
        if keep_going.lower().strip() == 'yes':
            first_check()
        elif keep_going.lower().strip() == 'no':
            print("Okay, thanks for using my app.")
        else:
            print("Your input is invalid, please try again.")
            less_more_equal()
    else:
        print(Fore.GREEN + f"{y} is more than {x}!")
        # The loop part:
        keep_going = input("Would you like to continue? Type yes or no: ")
        if keep_going.lower().strip() == 'yes':
            first_check()
        elif keep_going.lower().strip() == 'no':
            print("Okay, thanks for using my app.")
        else:
            print(Fore.RED + "Your input is invalid, please try again.")
            less_more_equal()


first_check()