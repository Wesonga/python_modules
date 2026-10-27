# Using return (Good practice for calculation functions)
def add_numbers(a, b):
    return a + b

# We capture the returned value in a variable
result = add_numbers(10, 5)
print(result)  # Output: 15

# We can even use it in further logic
final_price = add_numbers(100, 20) * 0.9  # 120 * 0.9
print(final_price)  # Output: 108.0