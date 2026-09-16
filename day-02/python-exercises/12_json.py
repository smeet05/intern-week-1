import json

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "salary": 45000
    },
    {
        "id": 102,
        "name": "Priya",
        "salary": 55000
    }
]

# Write JSON
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Employee data saved.")


# Read JSON
with open("employees.json", "r") as file:
    data = json.load(file)

print("\nEmployee data:")

for employee in data:
    print(employee)