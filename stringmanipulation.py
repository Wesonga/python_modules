
# Prompt the user for their first and last names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Modify the names using string methods
print("First name in uppercase:", first_name.upper())
print("Last name in lowercase:", last_name.lower())
print("Full name in title case:", (first_name + " " + last_name).title())

# Concatenate the first and last names
full_name = first_name + " " + last_name

# Calculate the total length of the full name
name_length = len(full_name)

# Reverse the full name
reversed_name = full_name[::-1]

# Check whether the full name contains the letter 'a'
contains_a = "a" in full_name.lower()

# Display the results
print("Full name:", full_name)
print("Total length of full name:", name_length)
print("Reversed full name:", reversed_name)
print("Contains the letter 'a':", contains_a)

print("Hello,", full_name.title() + "! Welcome.")
