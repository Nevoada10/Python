import random


def play_game(player_points, cpu_points):
    # Creating a list of choices.
    # Defining computer's choice.
    # Forcing the user to use one of the 3 options.
    while (player_points or cpu_points) < 2:

        # Defining stage:

        choices = ["ROCK", "PAPER", "SCISSORS"]
        player_won = "Player won!".upper()
        cpu_won = "CPU won!".upper()
        player_choice = None
        cpu_choice = (random.choice(choices)).upper()

        # Player choice stage:

        while player_choice not in choices:
            player_choice = (input("Choose Rock, Paper or Scissors: \n")).upper()

        # After choice, we need to check who won.
        # 1) If answer are the same it's a tie.
        # 2) If the user choose Rock, Paper or Scissors.

        tie = player_choice == cpu_choice
        if tie:
            cpu_points += 0
            player_points += 0
            print("IT'S A TIE")

        elif player_choice == "ROCK":
            if cpu_choice == "PAPER":
                cpu_points += 1
                print(cpu_won)
            elif cpu_choice == "SCISSORS":
                player_points += 1
                print(player_won)

        elif player_choice == "PAPER":
            if cpu_choice == "ROCK":
                print(player_won)
                player_points += 1
            elif cpu_choice == "SCISSORS":
                cpu_points += 1
                print(cpu_won)

        elif player_choice == "SCISSORS":
            if cpu_choice == "ROCK":
                cpu_points += 1
                print(cpu_won)
            elif cpu_choice == "PAPER":
                player_points += 1
                print(player_won)

        print("Player: {}, Computer: {}.".format(player_choice, cpu_choice))
        print("CPU Score: {}\nPlayer Score: {}\n".format(cpu_points, player_points))

    if player_points == 2:
        message = "You won!"

    elif cpu_points == 2:
        message = "You lost!"

    else:
        message = "It's a complete tie"

    print(message)


play_game(0, 0)
