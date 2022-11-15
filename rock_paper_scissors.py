import random


def rock_paper_scissors():
    print('Welcome to Rock Paper Scissor game!')
    should_continue = True
    comp_count = 0
    user_count = 0

    while should_continue:
        player_choice = input('Make your choice: [r - rock, p - paper, s - scissors]: ').lower()
        if player_choice not in ['r', 's', 'p']:
            print('Incorrect input. Try again')
            continue

        comp_choice = random.choice(['r', 's', 'p'])
        print(f'Compute choice is {comp_choice}')

        win_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

        if player_choice == comp_choice:
            print('A draw')
        elif (player_choice, comp_choice) in win_combinations:
            print('You win')
            user_count += 1
        else:
            print('Computer wins!')
            comp_count += 1

        should_continue = input('Want to proceed? [y/n]').lower()
        if should_continue == 'y':
            should_continue = True
        elif should_continue == 'n':
            print(f'It was pleasure to play with you!\nThe score is: Computer[{comp_count}] : You[{user_count}]')
            break
        else:
            print('Incorrect input. Try again')
            should_continue = input('Want to proceed? [y/n]').lower()
