#!/usr/bin/python3

from string_functions import string_compare

# Две ниже приведенные функции возвращают вложенный список.
# В первом индексе запись студента, во втором насколько совпадает ФИО исходя из функции string_compare
def my_list_triplet(in_var, triplet):
    result = []
    for i in in_var:
        val = string_compare(i[0],triplet)
        result.append([i[0], val])
        
    result.sort(key=lambda x: x[1],reverse=True)
    return result

def my_dict_triplet(in_var, triplet):
    result = []
    for i in in_var:
        tmpstr = i[1] + ' ' + i[0] + ' ' + i[2]
        val = string_compare(tmpstr, triplet)
        result.append([i, val])
        
    result.sort(key=lambda x: x[1],reverse=True)
    return result

# поиск студента, выводит одного самого совпадающего
def my_search(in_var,triplet):
    if(type(in_var) == list):
        tmp = my_list_triplet(in_var, triplet)
    elif(type(in_var) == dict):
        tmp = my_dict_triplet(in_var, triplet)
        
    if tmp[0][1] == 0: # не найдено похожих вообще
        return None
    
    return tmp[0]

# сравнение элементов между собой
def my_compare(in_var, in_var2):
    if(type(in_var2) == list):
        tmpstr = in_var2[0]
    elif(type(in_var2) == tuple):
        tmpstr = in_var2[1] + ' ' + in_var2[0] + ' ' + in_var2[2]
        
    if(type(in_var) == list):
        result = my_list_triplet(in_var, tmpstr)
    elif(type(in_var) == dict):
        result = my_dict_triplet(in_var, tmpstr)

    return result

