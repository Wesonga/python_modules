
# Prompt the user to enter a student's score
score = float(input("Enter the student's score (0-100): "))

# Check whether the score is valid
if score < 0 or score > 100:
    print("Invalid score! Please enter a score between 0 and 100.")

# Assign a grade if the score is valid
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Display the grade and a message
    print("Your grade is:", grade)

    if grade == "F":
        print("Keep practicing. You can improve!")
    else:
        print("Congratulations! Keep up the good work.")
