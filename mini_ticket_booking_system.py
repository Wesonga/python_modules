age = int(input("Enter your age: "))
student_id = input("Do you have student id(yes/no): ").lower()
movie_time = int(input("Enter movie time(24-hour format): "))


if age > 18:
    print("You can book the ticket.") 
elif age == 18:
    print("You can book the ticket")
elif age < 18 and student_id == "yes":
    if movie_time < 1800:
        print("You can book the ticket.")
    else:
        print("Sorry,You can book only before 1800hrs")
else:
    print("You are not eligible to book a ticket.")
    