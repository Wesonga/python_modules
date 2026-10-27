def calculate_sum():
    # i. Prompt the user for a positive integer limit and a choice
    try:
        limit = int(input("Enter a positive integer limit: "))
        if limit < 1:
            print("Please enter a number greater than 0.")
            return
            
        choice = input("Do you want to sum 'even' or 'odd' numbers? ").strip().lower()
        if choice not in ['even', 'odd']:
            print("Invalid choice. Please type 'even' or 'odd'.")
            return
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Initialize variables
    current_number = 1 if choice == 'odd' else 2
    total_sum = 0

    # ii. Use a while loop to iterate and add numbers to a running sum
    while current_number <= limit:
        total_sum += current_number
        current_number += 2  # Skip by 2 to only hit matching even/odd numbers

    # iii. Print the final sum
    print(f"The sum of {choice} numbers up to {limit} is: {total_sum}")

if __name__ == "__main__":
    calculate_sum()