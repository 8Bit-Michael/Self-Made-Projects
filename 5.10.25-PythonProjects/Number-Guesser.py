import random
print("""Welcome to my Number Guesser! Enter a starting number and an ending number
and I will create a number for you to guess in between them!""")

# The Input Part:
start = input('Enter your starting number: ')
end = input('Enter your ending number: ')
if not start.isdigit() or not end.isdigit():
    print('Please enter valid numbers.')
else:
    start = int(start)
    end = int(end)
    if start >= end:
        print('Please enter a valid range, the starting number cannot be greater than or equal to the ending number.')
    else:
        # The guessing part:
        number = random.randint(start, end)
        guess = None
        while guess != number:
            print('I have created a number between', start, 'and', end, 'for you to guess!')
            guess = input('Enter a guess: ')
            if not guess.isdigit():
                print('Please enter a valid number.')
            else:
                guess = int(guess)
                if guess != number:
                    if guess < number:
                        print('Your guess is too low.')
                    if guess > number:
                        print('Your guess is too high.')
                else:
                    print('Congratulations! You guessed the number!')
                    break




        