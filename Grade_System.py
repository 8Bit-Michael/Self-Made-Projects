# "pip install colorama" must be done in the terminal before running this.
from colorama import init, Fore
init(autoreset=True)

def evaluation(grade_input):
    if grade_input >= 100:
        print(Fore.GREEN + "You have an A+ in your class!")
    elif grade_input >= 95:
        print(Fore.GREEN + "You have an A in your class!")
    elif grade_input >= 90:
        print(Fore.GREEN + "You have an A- in your class!")
    elif grade_input >= 87:
        print(Fore.GREEN + "You have a B+ in your class!")
    elif grade_input >= 83:
        print(Fore.YELLOW + "You have a B in your class!")
    elif grade_input >= 80:
        print(Fore.YELLOW + "You have a B- in your class!")
    elif grade_input >= 77:
        print(Fore.YELLOW + "You have a C+ in your class.")
    elif grade_input >= 73:
        print(Fore.YELLOW + "You have a C in your class.")
    elif grade_input >= 70:
        print(Fore.YELLOW + "You have a C- in your class.")
    elif grade_input >= 67:
        print(Fore.YELLOW + "You have a D+ in your class.")
    elif grade_input >= 60:
        print(Fore.RED + "You have a D in your class.")
    elif grade_input >= 0:
        print(Fore.RED + "You have an F in your class.")
    else:
        print(Fore.RED + f"The grade {grade_input} isn't valid. Grades can't be negative.")

def retry():
    y_or_n = input("Would you like to check another grade? Type yes or no: ").strip().lower()
    if y_or_n == 'yes':
        print("Okay, let's keep going!\n")
        main()
    elif y_or_n == 'no':
        print("Okay, goodbye!")
    else:
        print(f"{y_or_n} isn't a valid input.")
        retry()

def main():
    user_input = input("Please enter a grade: ").strip()
    try:
        grade_input = int(user_input)
        evaluation(grade_input)
    except ValueError:
        print(Fore.RED + "Your input is invalid, please enter a number.")
    retry()

# The program's actual start:
main()