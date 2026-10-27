
# Shopping List Validator

# i. Initialize an empty list
shopping_list = []

# ii. Use a while loop to collect items
while True:
    item = input("Enter a shopping item (or type 'done' to finish): ")

    # iii. Check if the input is empty
    if item.strip() == "":
        print("Error: Item cannot be empty. Try again.")
        continue

    # Stop when the user types done
    if item.strip().lower() == "done":
        break

    # v. Check for duplicates
    if item.strip().lower() in [x.lower() for x in shopping_list]:
        print("This item is already on your shopping list!")
        continue

    # Add the valid item
    shopping_list.append(item.strip())
    print(f"Added: {item.strip()}")

# iv. Print the final shopping list
print("Your final shopping list:")

if len(shopping_list) == 0:
    print("Your shopping list is empty.")
else:
    for number, item in enumerate(shopping_list, start=1):
        print(f"{number}. {item}")

print(f"Total items: {len(shopping_list)}")
