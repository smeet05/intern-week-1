# Problem: Find the second largest element in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Second largest element:", second_largest)