fruits = ["apple", "banana", "cherry", "date"]
print(fruits[-1])
print(fruits[1:4])
print(fruits[:3])
print(fruits[-3:-1])

fruits.append("elderberry") #adds an element
fruits.insert(1, "blueberry") # inserts an element at a specific index
fruits.remove("banana") # removes an element by value
fruits.pop() # removes the last element
del fruits[0] # deleting by index 


print(fruits.count("dates"))

numbers = [2, 9, 1, 7, 3, 0] 
numbers.sort()
numbers.reverse()
print(numbers.count(1))


