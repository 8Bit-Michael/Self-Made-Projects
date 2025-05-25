# "pip install colorama" must be done in the terminal before running this.
from colorama import init, Fore
init(autoreset=True)
import re
import csv

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
    y_or_n = input("Would you like to enter a grade or check your grades? Type 'enter' or 'check': ").strip().lower()
    if y_or_n == 'enter':
        print("Okay, let's keep going!\n")
        main()
    elif y_or_n == 'check':
        # This lets you read the CSV file:
        with open('Grading_System.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print(Fore.RED + f"'{y_or_n}' isn't a valid input.")
        retry()
def is_valid_name(name):
    return bool(re.fullmatch(r"[A-Za-z'-]+", name))

def main():
    user_name = input("Please enter your first name: ").strip()
    if not is_valid_name(user_name):
        print(Fore.RED + f"'{user_name}' isn't a valid name. Names should only contain letters.")
        return
    else:
        print(Fore.GREEN + f"Your name has been saved to a CSV file, {user_name}!")
        user_input = input("Please enter one of your grades: ").strip()
        try:
            # This rounds a grade, like 99.99, into a whole number, like 100:
            grade_input = float(user_input)
            grade_input = round(grade_input)
            grade_input = int(grade_input)
            evaluation(grade_input)
            # This writes the input to a CSV file:
            with open('Grading_System.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_name, grade_input])
        except ValueError:
            print(Fore.RED + f"'{user_input}' is not a valid input, please enter a number.")
        retry()

# The program's actual start:
main()