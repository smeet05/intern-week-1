filename = "sample.txt"

# Write to file
with open(filename, "w") as file:
    file.write("Employee Management System\n")
    file.write("Python File Handling\n")


# Read from file
with open(filename, "r") as file:
    content = file.read()

print("File content:")
print(content)