#!/usr/bin/python3

original_str = "xyzyxyzyxyxyzzxyxyzyxyxyz"
new_str = ""

for char in original_str:
    if char == 'x':
        new_str += 'y'
    else:
        new_str += char

print(new_str)
