import random


def guess_number():
    comp_count = 0
    user_count = 0
    print('Welcome to Guess Number game!')
    print('You have to guess my number in range 0-20 from 3 attempts')
    comp_number = random.randint(0, 21)
    attempts = range(3, 0, -1)
    for i in attempts:
        user_number = int(input(f'Enter number(you have {i} attempts): '))
        if i == 1 and user_number != comp_number:
            print("Sorry, you didn't guess my number")
            comp_count += 1
        elif user_number > comp_number:
            print('More than my number, try again!')
        elif user_number < comp_number:
            print('Less than my number, try again!')
        else:
            print(f'Bingo! My number was {comp_number}')
            user_count += 1
            break

    should_continue = True
    while should_continue:
        should_continue = input("Would you like to repeat? (y/n): ").lower()
        if should_continue == 'y':
            guess_number()
        elif should_continue == 'n':
            print(f'It was pleasure to play with you\nThe score is: Computer[{comp_count}] : You[{user_count}]')
            break
        else:
            print('Incorrect choice')
