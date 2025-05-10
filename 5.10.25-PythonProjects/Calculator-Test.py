print('Welcome to my Python calculator, enter 2 numbers and you will get the sum!')
a = input('Enter your first number: ')
b = input('Enter your second number: ')
# Checks for invalid inputs.
if not a.isdigit() or not b.isdigit():
    print('Please enter valid numbers.')

result = float(a) + float(b)
print(f'Your result is: {result}')
