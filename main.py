from guess_number import guess_number
from rock_paper_scissors import rock_paper_scissors


def main():

    print("Hello! Welcome to entertainment chat-bot")
    while True:
        user_choice = input('I have 2 games for you! Would like to play?[y/n] ')
        if user_choice == 'y':
            print('Choose the game:')
            user = input("\t1. Guess number\n\t2. Rock Paper Scissors\n\tIf you don't want to play press 'q': ")
            match user:
                case '1':
                    guess_number()
                case '2':
                    rock_paper_scissors()
                case 'q':
                    print('Have a nice day!')
                    break
                case _:
                    print('Incorrect choice')
        elif user_choice == 'n':
            print("It's a pity you are leaving...")
            break
        else:
            print('Incorrect choice, try again')
            main()


if __name__ == '__main__':
    main()
