import random

game_outcomes = {
    "Rock crushes Scissors": ("Rock", "Scissors"),
    "Rock crushes Lizard": ("Rock", "Lizard"),
    "Paper covers Rock": ("Rock", "Paper"),
    "Spock vaporizes Rock": ("Spock", "Rock"),
    "Scissors decapitate Lizard": ("Scissors", "Lizard"),
    "Scissors cut Paper": ("Scissors", "Paper"),
    "Spock smashes Scissors": ("Spock", "Scissors"),
    "Lizard eats Paper": ("Lizard", "Paper"),
    "Lizard poisons Spock": ("Lizard", "Spock"),
    "Paper disproves Spock": ("Paper", "Spock")
}

actions = ["Rock", "Paper", "Scissors", "Lizard",  "Spock"]


def game_welcome():
    print("Welcome to game of Rock Paper Scissors (Extended Version)")
    print("First to win three games wins. Good luck!")


def user_selection():
    user_input = input("Enter your choice Rock[R], Paper[P], Scissors[Sc], Lizard[L] or Spock[Sp]: ").capitalize()
    selection = " ".join([x for x in actions if x.startswith(user_input)])

    if user_input == "S":
        user_input = input("Did you mean Scissors or Spock?: ")
        selection = " ".join([x for x in actions if x.startswith(user_input)])

    elif selection in actions:
        print(f"You have chosen: {selection}")

    return selection


def computer_selection():
    selection = random.choice(actions)
    print(f"Computer has chosen: {selection}")
    return selection


def determine_winner(user_action, computer_action):
    win = 0
    lose = 0
    draw = 0

    for k, v in game_outcomes.items():
        if v == (user_action, computer_action):
            win = win + 1
            print(f"{k}. YOU WIN!")

        elif v == (computer_action, user_action):
            lose = lose + 1
            print(f"{k}. YOU LOSE!")

    if computer_action == user_action:
        draw = draw + 1
        print("IT'S A DRAW!")

    elif user_action not in actions:
        print("Inputted action not recognised. YOU LOSE!")
        lose = lose + 1

    return win, lose, draw
