import random
from os import cpu_count


player = 0
cpu = 0

print("Three points win the game!")

while player < 3 and cpu < 3:
    cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
    player_choice = input("Rock, Paper or Scissors: ")

    if player_choice.lower() == cpu_choice:
        print("Tie! No points!")
    elif player_choice.lower() == "Rock":
        if cpu_choice == "Scissors":
            player += 1
            print("Player wins! One Point!")

        elif cpu_choice == "Paper":
            cpu += 1
            print("CPU wins! One Point!")

    elif player_choice.lower() == "Scissors":
        if cpu_choice == "Paper":
            player += 1
            print("Player wins! One Point!")

        elif cpu_choice == "Rock":
            cpu += 1
            print("CPU wins! One Point!")

    elif player_choice.lower() == "Paper":
        if cpu_choice == "Rock":
            player += 1
            print("Player wins! One Point!")

        elif cpu_choice == "Scissors":
            cpu += 1
            print("CPU wins! One Point!")

    else:
        print("Invalid input! New round!")

print("Player wins!" if player > cpu else "CPU wins!")
