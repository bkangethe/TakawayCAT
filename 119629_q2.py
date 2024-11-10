class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignments and grades

    def add_assignment(self, assignment_name, grade):
        """Add an assignment and its grade to the student's record."""
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        """Display all assignments and grades for the student."""
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print("No assignments found.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students in the course

    def add_student(self, student):
        """Add a student to the course."""
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        """Assign a grade to a student's assignment."""
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_grades(self):
        """Display all students and their grades for the course."""
        print(f"\nAll grades for {self.course_name}:")
        if self.students:
            for student in self.students:
                student.display_grades()
        else:
            print("No students enrolled in the course.")


# Interactive code
def main():
    # Create an instructor and a list of students
    instructor = Instructor("Dr. Smith", "Computer Science 101")

    while True:
        print("\nInstructor System")
        print("1. Add a Student")
        print("2. Assign a Grade")
        print("3. Display All Students' Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter student ID to assign grade: ")
            assignment_name = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade: "))
            except ValueError:
                print("Invalid input. Grade should be a number.")
                continue
            instructor.assign_grade(student_id, assignment_name, grade)

        elif choice == "3":
            instructor.display_all_students_grades()

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
