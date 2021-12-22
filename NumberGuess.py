# NumberGuess.py

import random

number = random.randint(1, 100)

tries = 0
found = False

while not found:
    guess = int(input("Guess a number between 1 and 10000: "))
    tries += 1
    if guess == number:
        found = True
        print(f"you found the number {number} after {tries} tries!")
    elif guess < number:
        print(f"The number you are looking for is less than {guess}!")

    else:
        print(f"The number you are looking for is less than {guess}!")
