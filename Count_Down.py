import time
# "pip install colorama" has to been installed using the terminal.
from colorama import init, Fore

init(autoreset=True)

def error_check():
    global user_number
    try:
        user_number = int(user_clock).__float__()
        print(f"Your timer will go off in {user_number} minutes, starting now.")
        countdown()
    except ValueError:
        print(Fore.RED + f"{user_clock} is not a valid input.")

def countdown():
    seconds = user_number * 60
    while seconds > 0:
        # The '\r' and end='' is added because it makes the text
        # look more clean and count down using one line in the terminal.
        print(Fore.GREEN + f"\rYou have {seconds} seconds left. ", end="")
        time.sleep(1)
        seconds -= 1
    print(Fore.RED + "\rYou've run out of time!            ")

user_clock = input("Please enter the minutes you would like on your countdown: ")
error_check()
