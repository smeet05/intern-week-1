# Problem: Reverse a given string.

def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")
print("Reversed:", reverse_string(text))