
# Sum of Even Numbers with While Loop

# i. Ask the user for a positive integer
limit = int(input("Enter a positive integer: "))

# Validate the input
if limit <= 0:
    print("Please enter a positive integer.")
else:
    total = 0
    number = 1

    # ii. Iterate through numbers up to the limit
    while number <= limit:
        if number % 2 == 0:
            total += number

        number += 1

    # iii. Print the final sum
    print(f"The sum of even numbers up to {limit} is {total}")
