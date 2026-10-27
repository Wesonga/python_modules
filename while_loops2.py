pin = 1234
attempts = 3
while attempts > 0:
    print(f"Attempts left: {attempts}")
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Access granted!")
        break
    elif pin != "1234":
        print("Wrong PIN!Please try again.")
    attempts -= 1
else:
    print("Out of attempts! Account locked.")
