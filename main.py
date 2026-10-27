
# main.py

import math_utils

try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        # Use functions from math_utils
        print("Number:", number)
        print("Is prime:", math_utils.is_prime(number))
        print("Square:", math_utils.square(number))
        print("Is even:", math_utils.is_even(number))
        print("Factorial:", math_utils.factorial(number))

except ValueError:
    print("Invalid input! Please enter a whole number.")
