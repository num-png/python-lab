#!/usr/bin/python3

num_array = [3,5,7,1,8,5,162,74,12,2,25,42,35,33]
result = 1

for num in num_array:
    if (num // 3 == num / 3) or (num // 5 == num / 5):
        result *= num

print(result)
