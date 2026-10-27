
import csv


class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = str(student_id)
        self.__grades = {}

    def add_grade(self, assignment, mark):
        assignment = assignment.strip() if isinstance(assignment, str) else ""

        if not assignment:
            raise ValueError("Assignment name cannot be empty.")

        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise TypeError("Mark must be a number.")

        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")

        self.__grades[assignment] = mark

    def get_average(self):
        if not self.__grades:
            return 0.0

        return sum(self.__grades.values()) / len(self.__grades)

    def get_grade(self, assignment):
        return self.__grades.get(assignment)

    def get_student_id(self):
        return self.__student_id

    def __str__(self):
        return (
            f"Student: {self.__name} | "
            f"ID: {self.__student_id} | "
            f"Average: {self.get_average()}%"
        )


class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
        self.__students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")

        if any(
            existing.get_student_id() == student.get_student_id()
            for existing in self.__students
        ):
            raise ValueError("A student with this ID already exists.")

        self.__students.append(student)

    def record_grade(self, student_id, assignment, mark):
        student_id = str(student_id)

        for student in self.__students:
            if student.get_student_id() == student_id:
                student.add_grade(assignment, mark)
                print(
                    f"Recorded {mark}% for student "
                    f"{student_id} in {assignment}."
                )
                return

        print(f"Error: Student ID {student_id} was not found.")

    def get_course_average(self):
        # Calculate the average of students' individual averages.
        students_with_grades = [
            student for student in self.__students
            if student.get_average() > 0
            or any(
                student.get_grade(assignment) == 0
                for assignment in ("Assignment 1", "Assignment 2",
                                   "Assignment 3", "Exam")
            )
        ]

        if not students_with_grades:
            return 0.0

        return sum(
            student.get_average() for student in students_with_grades
        ) / len(students_with_grades)

    def generate_report(self):
        print("\n" + "=" * 55)
        print(f"COURSE REPORT: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print("=" * 55)

        if not self.__students:
            print("No students registered.")
            return

        for student in self.__students:
            print(student)

        print("-" * 55)
        print(f"Course average: {self.get_course_average()}%")
        print("=" * 55)

    @classmethod
    def from_csv(
        cls, filename, course_name="Imported Course",
        instructor="Not specified"
    ):
        course = cls(course_name, instructor)

        with open(filename, mode="r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not {"name", "id"}.issubset(
                set(reader.fieldnames)
            ):
                raise ValueError(
                    "CSV must contain 'name' and 'id' column headers."
                )

            for row in reader:
                name = (row.get("name") or "").strip()
                student_id = (row.get("id") or "").strip()

                if not name or not student_id:
                    raise ValueError(
                        "Every CSV row must have a name and student ID."
                    )

                course.add_student(Student(name, student_id))

        return course


# -------------------------------
# Test the gradebook
# -------------------------------

course = Course("Python Programming", "Mr. Otieno")

# Create five students
students = [
    Student("Brian Wesonga", "ST001"),
    Student("Mary Wanjiku", "ST002"),
    Student("John Kamau", "ST003"),
    Student("Grace Akinyi", "ST004"),
    Student("Peter Mwangi", "ST005"),
]

# Add students to the course
for student in students:
    course.add_student(student)

# Record several grades for each student
grades = [
    ("ST001", "Assignment 1", 85),
    ("ST001", "Assignment 2", 90),
    ("ST001", "Exam", 88),

    ("ST002", "Assignment 1", 78),
    ("ST002", "Assignment 2", 82),
    ("ST002", "Exam", 80),

    ("ST003", "Assignment 1", 65),
    ("ST003", "Assignment 2", 70),
    ("ST003", "Exam", 68),

    ("ST004", "Assignment 1", 92),
    ("ST004", "Assignment 2", 95),
    ("ST004", "Exam", 94),

    ("ST005", "Assignment 1", 74),
    ("ST005", "Assignment 2", 76),
    ("ST005", "Exam", 79),
]

for student_id, assignment, mark in grades:
    course.record_grade(student_id, assignment, mark)

# Generate the final report
course.generate_report()
