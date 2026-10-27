# 1. Writing to a file (creates 'notes.txt' if it doesn't exist)
with open("notes.txt", "w") as file:
    file.write("Hello, file handling!\n")
    file.write("Learning Python is fun.\n")

# 2. Appending new data to the file
with open("notes.txt", "a") as file:
    file.write("This is a new appended line.\n")

# 3. Reading from the file
with open("notes.txt", "r") as file:
    content = file.read()
    print("--- File Contents ---")
    print(content)