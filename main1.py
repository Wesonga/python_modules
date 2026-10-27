
# Text File Reader

try:
    # Open and read the file safely
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Display file contents
    print("File contents:")
    for line in lines:
        print(line, end="")

    # Count the lines
    print("Number of lines:", len(lines))

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

except OSError:
    print("Error: The file could not be read.")
