# Problem: Find common elements in two arrays.

array1 = list(map(int, input("Enter first array: ").split()))
array2 = list(map(int, input("Enter second array: ").split()))

common = []

for number in array1:
    if number in array2 and number not in common:
        common.append(number)

print("Common elements:", common)