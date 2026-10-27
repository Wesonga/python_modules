
print("--- Boolean Logic Quiz Program ---")

try:
    # Prompt user for input and convert to float
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Step ii: Evaluate conditions using comparison and logical operators[cite: 1]
    both_positive = (num1 > 0) and (num2 > 0)
    first_larger = num1 > num2
    are_equal = num1 == num2
    at_least_one_negative = (num1 < 0) or (num2 < 0)
    not_equal = (num1 != num2)

    # Check if both numbers are even using the modulo operator (%)
    both_even = (num1 % 2 == 0) and (num2 % 2 == 0)

    # Print the boolean results with descriptive messages
    print("\n--- Evaluation Results ---")
    print(f"Inputs Received: num1 = {num1}, num2 = {num2}")
    print(f"1. Both numbers are positive (> 0): {both_positive}")
    print(f"2. First number is greater than the second (>): {first_larger}")
    print(f"3. Both numbers are equal (==): {are_equal}")
    print(f"4. At least one number is negative (< 0): {at_least_one_negative}")
    print(f"5. Numbers are NOT equal (not ==): {not_equal}")
    print(f"6. (Modification) Both numbers are even (%): {both_even}")

except ValueError:
    print("Invalid input! Please enter valid numeric values.")