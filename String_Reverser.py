import time
def user_process(): 
    user_input = input("Welcome to my reverse text generator, type in a string and you'll get an output: ")
    
    if user_input.isdigit():
        print("Your input is invalid")
    else:
        reversed_input = user_input[::-1]
        print(f'Your output is "{reversed_input}"')
        time.sleep(2)
        # The part which triggers the question asking if you want to continue:
        replay_again()

def validate():
    replay_again()

def replay_again():
    loop_input = input("Would you like to keep going? Type Yes or No: ")
    if loop_input == "Yes":
        print("Okay, let's keep going then!")
        user_process()
    elif loop_input == "No":
        print("Okay, thanks for trying out my app!")
    else:
        print("Your input is not valid.")
        validate()
        
# Where the code actually starts:
user_process()

