# fibonacci.py


def generate_fibonacci(limit=1000):

    a, b = 10, 11
    series = []
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    print(
        "Fibonacci series up to 1000:",
        generate_fibonacci(1000),
    )
