from os import strerror
import sys

filename = input("Input the file name: ")

try:
    f = open(filename, "r", encoding="utf-8")   # open the file in text mode
    text = f.read()                             # read the whole file into a string
    f.close()
except OSError as e:
    print("Error opening file:", strerror(e.errno))
    sys.exit(1)

text = text.lower()   # make everything lowercase

# Dictionary to store letter counts
counts = {}

# Loop over the file contents
for ch in text:
    if ch.isalpha():                  # only count letters
        if ch in counts:
            counts[ch] += 1           # increment if it exists
        else:
            counts[ch] = 1            # create new entry if not

# Print in alphabetical order
for letter in sorted(counts.keys()):
    print(letter, "->", counts[letter])
