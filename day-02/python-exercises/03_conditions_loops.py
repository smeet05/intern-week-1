marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


print("\nNumbers from 1 to 10:")

for number in range(1, 11):
    print(number)


print("\nWhile loop:")

count = 1

while count <= 5:
    print(count)
    count += 1