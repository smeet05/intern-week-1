class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)


class Manager(Employee):

    def show_role(self):
        print("Role: Manager")


manager = Manager("Rahul")

manager.display()
manager.show_role()