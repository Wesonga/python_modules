age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

if age >= 18:
    print("You are eligible to drink.")
    if height >= 150:
        print("Your height matches your age.")
    else:
        print("Show your ID to verify your age.")
else:
    print("Sorry, You are not eligible to drink.")
