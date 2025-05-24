from pathlib import Path
import csv
from colorama import init, Fore

init(autoreset=True)

file_path = Path("output.csv")

def add_contact():
    start = input("""Hi, is there anybody you would like to add to your contact book?
Type yes or no: """).lower().replace(",", "").replace("-", "").replace(".","").strip()

    if start == 'yes':
        first_name = input("Please enter their first name: ").strip()
        last_name = input("Now enter the last name of the person: ").strip()
        number = input(f"Finally, type in {first_name} {last_name}'s number: ").replace("-", "").strip()

        try:
            int(number)  # This makes sure that the input is a number.
        except ValueError:
            print(Fore.RED + f"{number} is not a valid number, try again.")
            return

        add_to_csv(first_name, last_name, number)

    elif start == 'no':
        review_or_not = input("Would you like to review your past contacts? Type yes or no: ").lower().strip()
        if review_or_not == 'yes':
            if file_path.exists():
                with open(file_path, mode="r", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            else:
                print(Fore.YELLOW + "No contacts found yet.")
        elif review_or_not == 'no':
            print("Okay, thank you for using my contact book project.")
        else:
            print(Fore.RED + f"{review_or_not} is not a valid input, try again.")
    else:
        print(Fore.RED + f"{start} is not a valid input.")

def add_to_csv(first_name, last_name, number):
    # If the file doesn't exist, create it with a header:
    file_exists = file_path.exists()
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["First Name", "Last Name", "Phone Number"])
        writer.writerow([first_name, last_name, number])

    print(Fore.GREEN + f"The contact {first_name} {last_name}, whose number is {number}, has been added.")

add_contact()
