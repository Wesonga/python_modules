# sequence based for loops in python
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    
    
# Range based for loops in python   
for i in range(5):
    print("wednesday")  # must be a string or defined
    
    
# Enumerate loop : used when you need index position and items value simultaneously.
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(f"index {index}:{fruit}")

    
# dictionary loop:iterate over keys,values or both key-value pairs
scores = {"alice":74, "brian":64}
for name, score in scores.items():
    print(f"{name} scored {score}")
  
  
# parallel loop using zip:used when you need to loop through two or more separate sequence simultaneously pairing, matching elements together
names = ["Anna", "Ben", "Brian"]
ages = [20, 22, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
