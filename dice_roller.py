# Dice Roller with Random

import random


# ii. Function to roll the dice
def roll_dice(sides, rolls):
    results = []

    for i in range(rolls):
        result = random.randint(1, sides)
        results.append(result)

    return results


# v. Function to calculate the sum and average
def calculate_statistics(results):
    total = sum(results)
    average = total / len(results)

    return total, average


# iii. Get input from the user
try:
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))

    if sides < 2:
        print("The dice must have at least 2 sides.")
    elif rolls < 1:
        print("You must roll the dice at least once.")
    else:
        # iv. Roll the dice
        results = roll_dice(sides, rolls)

        print("Dice roll results:", results)

        # Calculate statistics
        total, average = calculate_statistics(results)

        print("Sum of rolls:", total)
        print(f"Average of rolls: {average}")

except ValueError:
    print("Invalid input! Please enter whole numbers.")
