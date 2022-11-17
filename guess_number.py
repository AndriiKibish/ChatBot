import random


def guess_number():
    print('Welcome to Guess Number game!')
    print('You have to guess my number in range 0-20 from 3 attempts')
    comp_number = random.randint(0, 21)
    attempts = range(3, 0, -1)
    for i in attempts:
        user_number = int(input(f'Enter number(you have {i} attempts): '))
        if i == 1 and user_number != comp_number:
            print("Sorry, you didn't guess my number")
        elif user_number > comp_number:
            print('More than my number, try again!')
        elif user_number < comp_number:
            print('Less than my number, try again!')
        else:
            print(f'Bingo! My number was {comp_number}')
            break

    should_continue = True
    while should_continue:
        should_continue = input("Would you like to repeat? (y/n): ").lower()
        if should_continue == 'y':
            guess_number()
        elif should_continue == 'n':
            print('It was pleasure to play with you.')
            break
        else:
            print('Incorrect choice')
