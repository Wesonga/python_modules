age = int(input("Enter your age: "))
show_time = int(input("Enter the show time(use 24 hour format): "))



if age > 18 and show_time <= 22:
    print("You are allowed to watch the R-rated movie")
elif age == 18 and show_time > 22:
    print("Past bed time!")
else:
    print("Sorry, you must be 18 years and above to watch the R-rated movie.")
