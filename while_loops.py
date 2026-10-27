# sentinel-controlled while loop: used when the loop runs indefinetly until a specific input, event or "sentinel value" is encountered
password = ""
while password != "wesonga":
    password = input("Enter the password: ")
print("Access granted!")


# counter-controlled while loop: used when you want to run a specific number of time based on a changing counter variable'
count = 1
while count <= 3:
    print(f"Attempt {count}")
    count += 1
