
import csv

try:
    students = []

    # Open and read the CSV file
    with open("grades.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Validate the column headings
        if not reader.fieldnames or not {"name", "score"}.issubset(
            set(reader.fieldnames)
        ):
            raise ValueError("CSV must contain name and score columns.")

        for row in reader:
            name = (row.get("name") or "").strip()
            score_text = (row.get("score") or "").strip()

            if not name or not score_text:
                raise ValueError("A student name or score is missing.")

            try:
                score = float(score_text)
            except ValueError:
                raise ValueError(
                    f"Invalid score for {name}: {score_text}"
                ) from None

            if not 0 <= score <= 100:
                raise ValueError(
                    f"Score for {name} must be between 0 and 100."
                )

            students.append({"name": name, "score": score})

    if not students:
        print("No student grades found in the file.")
    else:
        scores = [student["score"] for student in students]

        # Calculate average, highest and lowest grades
        average = sum(scores) / len(scores)
        highest = max(students, key=lambda student: student["score"])
        lowest = min(students, key=lambda student: student["score"])

        print("STUDENT GRADE REPORT")

        for student in students:
            print(f"{student['name']}: {student['score']}")

        print(f"\nAverage grade: {average}")
        print(
            f"Highest grade: {highest['name']} "
            f"({highest['score']})"
        )
        print(
            f"Lowest grade: {lowest['name']} "
            f"({lowest['score']})"
        )

except FileNotFoundError:
    print("Error: grades.csv was not found.")

except OSError as error:
    print(f"File error: {error}")

except ValueError as error:
    print(f"Invalid data: {error}")
