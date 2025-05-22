def tips(order):
    if order == '1':
        with_tax = 10 * 1.5
        print(f"Your total is ${with_tax}.")
    elif order == '2':
        with_tax = 13 * 1.5
        print(f"Your total is ${with_tax}.")
    elif order == '3':
        with_tax = 12 * 1.5
        print(f"Your total is ${with_tax}.")
    elif order == '4':
        with_tax = 15 * 1.5
        print(f"Your total is ${with_tax}.")
    else:
        print("Your input isn't valid, try again.")
        retry()

def retry():
    order = input("""Welcome to my pizza app. Which pizza would you like?
    1. Classic cheese pizza. $10
    2. Pepparoni pizza. $13
    3. Stuffed crust pizza. $12
    4. Hawaiian style pizza. $15
    Type in the number you want: """)       
    tips(order)

# The actual start of the program:
order = input("""Welcome to my pizza app. Which pizza would you like?
1. Classic cheese pizza. $10
2. Pepparoni pizza. $13
3. Stuffed crust pizza. $12
4. Hawaiian style pizza. $15
Type in the number you want: """)

tips(order)
