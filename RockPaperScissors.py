import random

win = 0
lose = 0
draw = 0

play_game = input("Play Rock, Paper, Scissors (Y/N): ")
while play_game.upper() != "N":
    # Prompt the user to enter a value: R, P, S
    user_action = input("Enter your choice (R, P or S): ")
    # convert user input into Rock, Paper or Scissors respectively.
    if user_action.upper() == "R":
        user_action = "Rock"
    elif user_action.upper() == "P":
        user_action = "Paper"
    elif user_action.upper() == "S":
        user_action = "Scissors"

    # Ask the computer to generate a random value between 0 and 2
    computer_action = random.randint(0, 2)

    # Convert the computer's choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
    if computer_action == 0:
        computer_action = "Rock"

    elif computer_action == 1:
        computer_action = "Paper"

    elif computer_action == 2:
        computer_action = "Scissors"

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    # Compare the user's choice with the computer's choice
    # Display message indicating whether the user won, lost or drew against the computer.

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a draw!")
        draw = draw + 1
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
            win = win + 1
        else:
            print("Paper covers Rock. You lose.")
            lose = lose + 1
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
            win = win + 1
        else:
            print("Scissors cut Paper! You lose!")
            lose = lose + 1
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cut Paper! You win!")
            win = win + 1
        else:
            print("Rock smashes Scissors! You lose!")
            lose = lose + 1

    print(f"\nGames won = {win}\nGames lost = {lose}\nGames drawn = {draw}")

    play_game = input("\nPlay again (Y/N)?: ")
    if play_game.upper() != "Y":
        break

