def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    return total_salary


basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))

salary = calculate_salary(basic, bonus)

print("Total salary:", salary)