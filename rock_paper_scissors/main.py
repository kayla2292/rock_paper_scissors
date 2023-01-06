import random
picks = ['rock', 'paper', 'scissors']

def rockPaperScissors():
    print("Welcome to Rock, Paper, Scissors! Lets Play!")
    name = input("My name is RPS Master. What is your name? ")
    counter = 0

    quit = False
    while quit == False:
        counter += 1
        random_choice = random.choice(picks)
        user_choice = input(f'\nYour move {name}! Pick either... Rock, Paper, or Scissors! ')
        if user_choice.lower() == 'i quit':
            print('\nThank you for playing! Until next time!')
            quit = True
        elif user_choice.lower() == 'rock':
            if random_choice == 'rock':
                print(f"You chose {user_choice.title()}, so did I. Game Tied!")
            elif random_choice == 'paper':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You lose!")
            elif random_choice == 'scissors':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You win!")
        elif user_choice.lower() == 'paper':
            if random_choice == 'paper':
                print(f"You chose {user_choice.title()}, so did I. Game Tied!")
            elif random_choice == 'scissors':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You lose!")
            elif random_choice == 'rock':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You win!")
        elif user_choice.lower() == 'scissors':
            if random_choice == 'scissors':
                print(f"You chose {user_choice.title()}, so did I. Game Tied!")
            elif random_choice == 'rock':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You lose!")
            elif random_choice == 'paper':
                print(f"You chose {user_choice.title()}, I chose {random_choice.title()}. You win!")
        #elif user_choice.lower() != 'i quit' and user_choice.lower() not in picks:
        else:
            print('Sorry! Not a valid choice. Try again!')
        if counter >= 3 and user_choice.lower() != 'i quit':
            quit_choice = input('Hey! You been playing for awhile now... If you would like to quit, please type "I quit". Otherwise, type "continue": ')
            if quit_choice.lower() == 'i quit':
                print('\nThank you for playing! Until next time!')
                quit = True
            else:
                counter = 0
                continue





rockPaperScissors()