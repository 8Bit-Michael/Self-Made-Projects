def the_loop():
    print("Welcome to my small Python 'reflection' test. Enter in a phrase and it will be repeated: ")
    user_line = input()
    print(f"Reflection: {user_line}.")
    print("Would you like to continue? Press Y for yes and N for no: ")
    
    choice = input().strip().upper()

    if choice == 'Y':
        the_loop()
    elif choice == 'N':
        print("Okay, goodbye then.")
    else:
        print("Invalid input!")
        exit()

the_loop()



