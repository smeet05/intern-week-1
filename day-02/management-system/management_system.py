import json


FILE_NAME = "employees.json"


def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []


def save_employees():
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


def add_employee():
    try:
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        employee = {
            "id": employee_id,
            "name": name,
            "salary": salary,
            "department": department
        }

        employees.append(employee)
        save_employees()

        print("Employee added successfully.")

    except ValueError:
        print("Invalid input.")


def update_employee():
    try:
        employee_id = int(input("Enter employee ID to update: "))

        for employee in employees:

            if employee["id"] == employee_id:

                employee["name"] = input("Enter new name: ")
                employee["salary"] = float(input("Enter new salary: "))
                employee["department"] = input("Enter new department: ")

                save_employees()

                print("Employee updated successfully.")
                return

        print("Employee not found.")

    except ValueError:
        print("Invalid input.")


def delete_employee():
    try:
        employee_id = int(input("Enter employee ID to delete: "))

        for employee in employees:

            if employee["id"] == employee_id:

                employees.remove(employee)
                save_employees()

                print("Employee deleted successfully.")
                return

        print("Employee not found.")

    except ValueError:
        print("Invalid input.")


def search_employee():
    try:
        employee_id = int(input("Enter employee ID to search: "))

        for employee in employees:

            if employee["id"] == employee_id:

                print("\nEmployee found:")
                print("ID:", employee["id"])
                print("Name:", employee["name"])
                print("Salary:", employee["salary"])
                print("Department:", employee["department"])

                return

        print("Employee not found.")

    except ValueError:
        print("Invalid input.")


def filter_department():
    department = input("Enter department: ")

    found = False

    for employee in employees:

        if employee["department"].lower() == department.lower():

            print(employee)
            found = True

    if not found:
        print("No employees found.")


def sort_employees():
    if len(employees) == 0:
        print("No employees found.")
        return

    sorted_employees = sorted(
        employees,
        key=lambda employee: employee["salary"]
    )

    print("\nEmployees sorted by salary:")

    for employee in sorted_employees:
        print(employee)


def statistics():
    if len(employees) == 0:
        print("No employees found.")
        return

    total_salary = 0

    highest = employees[0]
    lowest = employees[0]

    for employee in employees:

        total_salary += employee["salary"]

        if employee["salary"] > highest["salary"]:
            highest = employee

        if employee["salary"] < lowest["salary"]:
            lowest = employee

    average = total_salary / len(employees)

    print("\n===== Statistics =====")
    print("Total employees:", len(employees))
    print("Average salary:", average)
    print("Highest salary:", highest["salary"])
    print("Lowest salary:", lowest["salary"])


def list_employees():
    if len(employees) == 0:
        print("No employees found.")
        return

    print("\n===== Employee List =====")

    for employee in employees:

        print("--------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Salary:", employee["salary"])
        print("Department:", employee["department"])


employees = load_employees()


while True:

    print("\n===== Employee Management System =====")

    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. List Employees")
    print("6. Filter by Department")
    print("7. Sort by Salary")
    print("8. Statistics")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        update_employee()

    elif choice == "3":
        delete_employee()

    elif choice == "4":
        search_employee()

    elif choice == "5":
        list_employees()

    elif choice == "6":
        filter_department()

    elif choice == "7":
        sort_employees()

    elif choice == "8":
        statistics()

    elif choice == "9":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")