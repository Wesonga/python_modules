
# Import the random module
import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize the number of attempts
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")
print("You have 5 attempts to guess correctly.")

# Continue the game while attempts remain
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    # Increase the attempt counter
    attempts += 1

    # Compare the guess with the target number
    if guess == target_number:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", attempts)
        break
    elif guess < target_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

# Check if the player used all attempts
if attempts == max_attempts and guess != target_number:
    print("Game over! You have used all your attempts.")
    print("The correct number was:", target_number)
