
print("--- Personal Monthly Budget Calculator ---")

try:
    # Prompt user for monthly income and major expenses
    income = float(input("Enter your total monthly income (Ksh): "))
    rent = float(input("Enter your monthly rent expense (Ksh): "))
    food = float(input("Enter your monthly food/groceries expense (Ksh): "))
    transport = float(input("Enter your monthly transport expense (Ksh): "))
    utilities = float(input("Enter your monthly utilities expense (Ksh): "))

    # Use arithmetic operators to compute total expenses and remaining budget
    total_expenses = rent + food + transport + utilities
    remaining_budget = income - total_expenses

    # Calculate percentage of income spent on each expense
    rent_pct = (rent / income) * 100 if income > 0 else 0
    food_pct = (food / income) * 100 if income > 0 else 0
    transport_pct = (transport / income) * 100 if income > 0 else 0
    utilities_pct = (utilities / income) * 100 if income > 0 else 0
    total_spent_pct = (total_expenses / income) * 100 if income > 0 else 0

    # Print results using formatted output (f-strings)
    print("           BUDGET SUMMARY REPORT       ")
    print(f"Monthly Income      : Ksh {income}")
    print(f"Total Expenses      : Ksh {total_expenses} ({total_spent_pct}% of income)")
    print(f"Remaining Budget    : Ksh {remaining_budget}")
    print(f"  • Rent      : Ksh {rent} ({rent_pct}%)")
    print(f"  • Food      : Ksh {food} ({food_pct}%)")
    print(f"  • Transport : Ksh {transport} ({transport_pct}%)")
    print(f"  • Utilities : Ksh {utilities} ({utilities_pct}%)")

    # Simple advisory condition
    if remaining_budget < 0:
        print(" Warning: You are operating at a deficit this month!")
    else:
        print("Great job keeping your expenses within your income limit.")

except ValueError:
    print("Invalid input! Please enter numeric values for income and expenses.")

