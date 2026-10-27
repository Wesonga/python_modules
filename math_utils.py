
# math_utils.py

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def square(num):
    """Return the square of a number."""
    return num ** 2


# Additional utility functions

def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result
