print("""
    +-------------------------------------------------------------------------------------------+
    |  Stone-Paper-Scissor is a very common game played by almost everyone in their childhood.  |
    |  Rules: There will be two players - here user and the computer.                           |
    |  On counting stone-paper-scissor, each player has to make any one of these in their hands.|
    |  Stone will damage scissor; scissor will cut the paper and paper can capture stone.       |
    |  Player with maximum points will win.                                                     |
    +-------------------------------------------------------------------------------------------+
""")

user_points = 0
computer_points = 0
i = 0
list_of_symbols = ['stone', 'paper', 'scissor']


while i < 10:
    user_choice = input("Enter your choice - stone, paper, scissor: ")
    import random
    computer_choice = random.choice(list_of_symbols)
    print("My choice:", computer_choice)

    if computer_choice == user_choice:
        i +=1
        print(f"It's a tie for round {i}. 0 for both of us.\n")

    elif computer_choice == 'stone' and user_choice == 'paper':
        user_points += 1
        i += 1
        print(f"You win round {i}. Point 1 for you!\n")

    elif computer_choice == 'paper' and user_choice == 'stone':
        computer_points += 1
        i += 1
        print(f"I win round {i}. Point 1 for me!\n")

    elif computer_choice == 'stone' and user_choice == 'scissor':
        computer_points += 1
        i += 1
        print(f"I win round {i}. Point 1 for me!\n")

    elif computer_choice == 'scissor' and user_choice == 'stone':
        user_points += 1
        i += 1
        print(f"You win round {i}. Point 1 for you!\n")

    elif computer_choice == 'paper' and user_choice == 'scissor':
        user_points += 1
        i += 1
        print(f"You win round {i}. Point 1 for you!\n")

    elif computer_choice == 'scissor' and user_choice == 'paper':
        computer_points += 1
        i += 1
        print(f"I win round {i}. Point 1 for me!\n")

    else:
        print("Invalid input. Try again!\n")

print(f"Your total score after ten rounds is {user_points}")
print(f"My total score after ten rounds is {computer_points}")
if user_points > computer_points:
    print(f"\nCongratulations! You win the game by {user_points - computer_points} points.\n")
else:
    print(f"\nHehe! I win the game by {computer_points - user_points} points. Better luck next time!\n")

