# Problem: Remove duplicates from a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("After removing duplicates:", unique_numbers)