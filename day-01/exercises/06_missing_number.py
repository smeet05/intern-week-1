# Problem: Find the missing number from 1 to n.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)