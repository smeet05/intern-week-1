import csv


FILE_NAME = "employees.csv"

employees = []


try:
    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

except FileNotFoundError:
    print("CSV file not found.")


print("Total records:", len(employees))


# Calculate salaries

salaries = []

for employee in employees:
    salaries.append(float(employee["salary"]))


if len(salaries) > 0:

    average = sum(salaries) / len(salaries)

    print("Average salary:", average)
    print("Minimum salary:", min(salaries))
    print("Maximum salary:", max(salaries))


# Department statistics

department_count = {}

for employee in employees:

    department = employee["department"]

    if department in department_count:
        department_count[department] += 1
    else:
        department_count[department] = 1


print("\nEmployees by department:")

for department, count in department_count.items():

    print(department, ":", count)


# Check missing values

print("\nMissing values:")

for employee in employees:

    for field, value in employee.items():

        if value == "":
            print(
                "Employee ID",
                employee["id"],
                "has missing",
                field
            )


# Check duplicate IDs

ids = []

for employee in employees:

    employee_id = employee["id"]

    if employee_id in ids:
        print("Duplicate ID:", employee_id)

    else:
        ids.append(employee_id)