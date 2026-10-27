# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# 1. Accessing items by index (counting starts at 0)
print(fruits[0])  # Output: apple

# 2. Modifying an item (Mutability in action)
fruits[1] = "blueberry"
print(fruits)     # Output: ['apple', 'blueberry', 'cherry']

# 3. Adding a new item using .append()
fruits.append("orange")
print(fruits)     # Output: ['apple', 'blueberry', 'cherry', 'orange']

# 4. Removing an item
fruits.remove("apple")
print(fruits)     # Output: ['blueberry', 'cherry', 'orange']