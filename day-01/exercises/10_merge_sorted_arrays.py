# Problem: Merge two sorted arrays.

array1 = list(map(int, input("Enter first sorted array: ").split()))
array2 = list(map(int, input("Enter second sorted array: ").split()))

merged = []

i = 0
j = 0

while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        merged.append(array1[i])
        i += 1
    else:
        merged.append(array2[j])
        j += 1

while i < len(array1):
    merged.append(array1[i])
    i += 1

while j < len(array2):
    merged.append(array2[j])
    j += 1

print("Merged array:", merged)