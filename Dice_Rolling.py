import random

user_score = 0

def begin_app():
    print("Welcome to my dice rolling app!")
    input("Press Enter to start rolling the dice...")
    randomize_results()

def randomize_results():
    global user_score
    while True:
        odds = random.randint(1, 6)
        user_score += odds
        print(f"{odds} has been added to your score!")

        while True:
            retry = input("Would you like to continue? Type Yes or No: ").strip().lower()
            if retry == "yes":
                break  
            elif retry == "no":
                print(f"\033[92mOkay, your total score is {user_score}!\033[0m")
                # Return stops the code from running.
                return
            else:
                print("That's not a valid answer, please type 'Yes' or 'No'.")

begin_app()
