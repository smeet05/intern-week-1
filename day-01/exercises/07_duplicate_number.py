# Problem: Find the duplicate number in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

duplicate = None

for number in numbers:
    if numbers.count(number) > 1:
        duplicate = number
        break

print("Duplicate number:", duplicate)