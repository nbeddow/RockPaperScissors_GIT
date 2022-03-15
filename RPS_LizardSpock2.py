from mymodules import lizardSpockModule as myModule
from operator import add


wins_losses_draws = (0, 0, 0)
myModule.game_welcome()
play_game = input("Play game (Y/N)?: ")
while play_game.upper() != "N" and wins_losses_draws[0] <= 3 and wins_losses_draws[1] <= 3:

    user_action = myModule.user_selection()
    computer_action = myModule.computer_selection()
    result = myModule.determine_winner(user_action, computer_action)
    wins_losses_draws = list(map(add, wins_losses_draws, result))

    # score tally
    print(f"\nGames won = {wins_losses_draws[0]} "
          f"\nGames lost = {wins_losses_draws[1]}"
          f"\nGames drawn = {wins_losses_draws[2]}")

    print("-"*100)

    # first to 3 wins
    if wins_losses_draws[0] == 3:
        play_game = input("YOU HAVE WON 3 GAMES! EXCELLENT! Play another round (Y/N)?: ")
        wins_losses_draws = (0, 0, 0)
        print("-" * 100)

    elif wins_losses_draws[1] == 3:
        play_game = input("YOU HAVE LOST 3 GAMES! GAME OVER! Play another round (Y/N)?: ")
        wins_losses_draws = (0, 0, 0)
        print("-" * 100)

    # repeat/end game
    if play_game.upper() != "Y":
        print("Thank you for playing!")
        break
