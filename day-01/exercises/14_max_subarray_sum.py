# Problem: Find the maximum subarray sum.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

current_sum = numbers[0]
maximum_sum = numbers[0]

for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    maximum_sum = max(maximum_sum, current_sum)

print("Maximum subarray sum:", maximum_sum)