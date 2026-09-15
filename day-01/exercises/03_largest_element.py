# Problem: Find the largest element in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest element:", largest)