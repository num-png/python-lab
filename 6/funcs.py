#!/usr/bin/python

# регистрозависимое нечеткое сравнение строкa
def string_compare_casesens(s1,s2):
    ngrams = [
        s1[i:i+3] for i in range(len(s1))
        ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count / max(len(s1), len(s2))

# регистронезависимое нечеткое сравнение строк
def string_compare(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    ngrams = [
        s1[i:i+3] for i in range(len(s1))
        ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count / max(len(s1), len(s2))

# регистронезависимое сравнение строк
def str_match(s1,s2):
    return s1.lower() == s2.lower()

# нечеткое сравнение чисел
def numrange_match(num,cmp,r):
    hi = cmp+r
    lo = cmp-r
    if ((num >= lo) and (num <= hi)):
        return True
    return False

# Имя - строгий поиск
def students_search_firstname(invar, s):
    result = {}
    
    for i in invar:
        if(invar[i].firstname.lower() == s.lower()):
            result[i] = invar[i]

    return result

# Имя - нестрогий поиск
def students_tryfind_firstname(invar, s):
    result = {}
    
    for i in invar:
        if(string_compare(invar[i].firstname,s) > 0.35):
            result[i] = invar[i]

    return result

# Высота - строгий поиск
def students_search_height(invar, num):
    result = {}
    
    for i in invar:
        if(invar[i].height == num):
            result[i] = invar[i]

    return result

# Высота - нечеткий поиск
def students_tryfind_height(invar, num):
    result = {}
    
    for i in invar:
        if(numrange_match(invar[i].height,num,5)):
            result[i] = invar[i]

    return result
