numbers = [1, 2, 3, 4, 5, 6]

squares = [number * number for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)