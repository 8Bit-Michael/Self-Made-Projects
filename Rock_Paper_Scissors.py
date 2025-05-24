import random
import time
# "pip install colorama" has to been installed using the terminal.
from colorama import init, Fore

init(autoreset=True)

def get_user_choice():
    while True:
        choice = input("""\nYou have three moves you can use:
            
    1. Rock - rock crushes scissors, and paper covers rock.
    2. Scissors - scissors can cut paper, but get crushed by the rock.
    3. Paper - paper can cover rock, but scissors can cut paper.

Type in the number you want to play as: """)
        if choice in ['1', '2', '3']:
            return choice
        else:
            print(Fore.RED + "That's not a valid input, please try again.")

def computer_response(user_choice):
    computer_choice = random.choice(['1', '2', '3'])
    moves = {'1': 'Rock', '2': 'Scissors', '3': 'Paper'}
    print(f"\nThe AI chose: {moves[computer_choice]}")
    print(f"You chose: {moves[user_choice]}")
    outcomes = {
        ('1', '2'): "Rock crushes scissors! You win!",
        ('2', '3'): "Scissors cut paper! You win!",
        ('3', '1'): "Paper covers rock! You win!",
        ('2', '1'): "Rock crushes scissors! You lose.",
        ('3', '2'): "Scissors cut paper! You lose.",
        ('1', '3'): "Paper covers rock! You lose.",
    }

    if user_choice == computer_choice:
        print(Fore.YELLOW + "It's a tie!")
    else:
        result = outcomes.get((user_choice, computer_choice))
        if "win" in result:
            print(Fore.GREEN + result)
        else:
            print(Fore.RED + result)

def game_start():
    user_choice = get_user_choice()
    computer_response(user_choice)

begin = input("Welcome to Rock, Paper, Scissors! Press Enter to begin: ")

# Error handling:
if begin == "":
    game_start()
else:
    print(Fore.RED + "Invalid input. Please restart and press Enter to begin.")

        

# The code actual start of the game:
begin = input("Welcome to Rock, Paper, Scissors! Type enter to begin: ")
game_start()