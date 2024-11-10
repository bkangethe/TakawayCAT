class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display employee details."""
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        """Update employee's salary."""
        self.salary = new_salary
        print(f"Salary for {self.name} updated to ${self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) has been added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        """Calculate and display total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: ${total_salary}")

    def display_all_employees(self):
        """Display all employees in the department."""
        print(f"\nEmployees in {self.department_name} department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")


# Interactive code
def main():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nDepartment Management System")
        print("1. Add an Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
            except ValueError:
                print("Invalid input. Salary should be a number.")
                continue
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            emp_id = input("Enter employee ID to update salary: ")
            employee = next((e for e in department.employees if e.employee_id == emp_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid input. Salary should be a number.")
            else:
                print(f"No employee found with ID {emp_id}.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display employee details."""
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        """Update employee's salary."""
        self.salary = new_salary
        print(f"Salary for {self.name} updated to ${self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) has been added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        """Calculate and display total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: ${total_salary}")

    def display_all_employees(self):
        """Display all employees in the department."""
        print(f"\nEmployees in {self.department_name} department:")
        if self.employees:
            for employee in self.employees:
                employee.display_details()
        else:
            print("No employees in this department.")


# Interactive code
def main():
    # Create a department
    department_name = input("Enter the department name: ")
    department = Department(department_name)

    while True:
        print("\nDepartment Management System")
        print("1. Add an Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: "))
            except ValueError:
                print("Invalid input. Salary should be a number.")
                continue
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            emp_id = input("Enter employee ID to update salary: ")
            employee = next((e for e in department.employees if e.employee_id == emp_id), None)
            if employee:
                try:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid input. Salary should be a number.")
            else:
                print(f"No employee found with ID {emp_id}.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
