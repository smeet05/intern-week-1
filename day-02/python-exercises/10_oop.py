class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Rahul", 45000)
employee2 = Employee("Priya", 55000)

employee1.display()

print()

employee2.display()