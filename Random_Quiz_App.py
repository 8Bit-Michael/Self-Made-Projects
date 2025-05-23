import random
import re
# "pip install colorama" has to been installed using the terminal.
from colorama import init, Fore, Style
init(autoreset=True)
score = 0

keep_going = input("Welcome to my Python quiz app! Press any key to continue: ")

with open('Quiz_App_Questions.txt', 'r') as file:
    questions = file.readlines()

questions = [q.strip() for q in questions if q.strip()]

def random_questions():
    random.shuffle(questions)

for question in questions:
    if "|" in question:
        question_text, correct_answer = question.split("|", 1)
        user_answer = input(question_text + " ")

        def sanitize(text):
            return re.sub(r'[^a-z0-9]', '', text.lower())

        if sanitize(user_answer) == sanitize(correct_answer):
            print(Fore.GREEN + "Correct!\n")
            score +=1
        else:
            print(Fore.RED + f"Wrong, the correct answer to question of {question_text} was {correct_answer}")
    else:
        print("The question was not formatted in a valid way.")
        random_questions()

