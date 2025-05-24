from pathlib import Path
import csv
from colorama import init, Fore

init(autoreset=True)

def survey_questions():
    question_1 = input("What types of food do you like: ").lower().replace(",", "").replace("-", "").strip()
    question_2 = input("What movie genres do you like: ").lower().replace(",", "").replace("-", "").strip()
    question_3 = input("What sports do you play: ").lower().replace(",", "").replace("-", "").strip()
    return [question_1, question_2, question_3]

file_path = Path("Survey_Program.csv")

# If the file doesn't exist, create it with a header:
if not file_path.exists():
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Food", "Movies", "Sports"])

# Get the user's input and append to CSV:
user_responses = survey_questions()
with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(user_responses)
    writer.writerow([])
    print(Fore.GREEN + "Your data has been saved to a CSV file!")