

print(" Student Grade Calculator ")

try:
    # Step i: Prompt the user to enter a score (0-100)
    score = float(input("Enter the student's score (0-100): "))

    # Modification Task: Add a check for invalid scores (below 0 or above 100)
    if score < 0 or score > 100:
        print(" Error: Invalid score! Please enter a value between 0 and 100.")
    else:
        # Step ii & iv: Use if-elif-else to determine the grade with explanatory comments
        if score >= 90:
            grade = "A"
            remark = "Excellent performance!"
        elif score >= 80:
            grade = "B"
            remark = "Very good job!"
        elif score >= 70:
            grade = "C"
            remark = "Good effort, passing grade."
        elif score >= 60:
            grade = "D"
            remark = "Fair, but needs improvement."
        else:
            grade = "F"
            remark = "Fail. Additional revision required."

        # Step iii: Print the grade with a descriptive message[cite: 1]
        print("\n" + "="*35)
        print(f"Score Entered : {score}")
        print(f"Assigned Grade: {grade}")
        print(f"Feedback      : {remark}")
        print("="*35)

except ValueError:
    print("Invalid input! Please enter a numerical score.") 