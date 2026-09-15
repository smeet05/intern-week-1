# Problem: Count the frequency of each character in a string.

text = input("Enter a string: ")

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

for character, count in frequency.items():
    print(character, ":", count)