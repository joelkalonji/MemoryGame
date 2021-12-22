import time
import os
import random


colors = "RGBY"

simon = ""

for score in range(0, 10):
    simon += random.choice(colors)
    for color in simon:
        print(simon)
        time.sleep(1.5)
        os.system("cls")
    guess = input("Repeat: ")
    os.system("cls")
    if guess != simon:
        break

print(f"Game Over! You final score is {score}!")