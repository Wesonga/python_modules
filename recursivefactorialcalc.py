
# Factorial Calculator Using Recursion

def factorial(n):
    # Base cases
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Get input from the user
try:
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Error: Please enter a non-negative integer.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")

except ValueError:
    print("Invalid input! Please enter a whole number.")
