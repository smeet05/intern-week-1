# Employee Management CLI

employees = []

def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    department = input("Enter employee department: ")

    employee = {
        "id": employee_id,
        "name": name,
        "salary": salary,
        "department": department
    }

    employees.append(employee)

    print("Employee added successfully.")

def update_employee():
    employee_id = input("Enter employee ID to update: ")

    for employee in employees:
        if employee["id"] == employee_id:
            employee["name"] = input("Enter new name: ")
            employee["salary"] = float(input("Enter new salary: "))
            employee["department"] = input("Enter new department: ")

            print("Employee updated successfully.")
            return

    print("Employee not found.")

def delete_employee():
    employee_id = input("Enter employee ID to delete: ")

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")

def search_employee():
    employee_id = input("Enter employee ID to search: ")

    for employee in employees:
        if employee["id"] == employee_id:
            print("\nEmployee found:")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Salary:", employee["salary"])
            print("Department:", employee["department"])
            return

    print("Employee not found.")

def list_employees():
    if len(employees) == 0:
        print("No employees found.")
        return

    print("\nEmployee List:")

    for employee in employees:
        print("--------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Salary:", employee["salary"])
        print("Department:", employee["department"])

def highest_salary():
    if len(employees) == 0:
        print("No employees found.")
        return

    highest = employees[0]

    for employee in employees:
        if employee["salary"] > highest["salary"]:
            highest = employee

    print("\nEmployee with Highest Salary:")
    print("ID:", highest["id"])
    print("Name:", highest["name"])
    print("Salary:", highest["salary"])
    print("Department:", highest["department"])

def average_salary():
    if len(employees) == 0:
        print("No employees found.")
        return

    total_salary = 0

    for employee in employees:
        total_salary += employee["salary"]

    average = total_salary / len(employees)

    print("\nAverage Salary:", average)

def department_filter():
    department = input("Enter department to filter: ")

    found = False

    for employee in employees:
        if employee["department"].lower() == department.lower():
            print("\nEmployee:")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Salary:", employee["salary"])
            print("Department:", employee["department"])
            found = True

    if not found:
        print("No employees found in this department.")

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. List Employees")
    print("6. Highest Salary")
    print("7. Average Salary")
    print("8. Department Filter")
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
        highest_salary()

    elif choice == "7":
        average_salary()

    elif choice == "8":
        department_filter()

    elif choice == "9":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")