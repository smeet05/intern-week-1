# Problem: Find the first non-repeating character in a string.

text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

for character in text:
    if frequency[character] == 1:
        print("First non-repeating character:", character)
        break
else:
    print("No non-repeating character found")