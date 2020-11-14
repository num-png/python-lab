#!/usr/bin/python3

list_arr= [
        ["Иван Петров М.", 1993, 5, 4, 4],
        ["Петр Андреев В.", 1997, 5, 5, 5],
        ["Артем Евгеньев А.", 1992, 4, 3, 5],
        ["Виктория Артемова М.", 1991, 3, 3, 5]
        ]       

# самый молодой студент (список)
max_year = 0
youngest = None 

for i in list_arr:
    if max_year <= i[1]:
        max_year = i[1]
        youngest = i
print("Самый молодой студент (список)")
print(youngest[0] + ' родился в ' + str(max_year))

