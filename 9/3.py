#!/usr/bin/python

import random
from string_functions import *

words_to_remove = ["может", "ли", "быть", "такое", "возможно", "если", "как", "почему", "будет",
                   "что ли", "что", "а", "же", "так"]

sym_to_remove = ["!","?",",",".","\\","/","*"]

if __name__ == "__main__":
    history = {}
    
    try:
        while True:
            curanswer = None
            curstr = None
            tmplist = []
            
            print("---")
            print("Введите вопрос:")
            
            curstr = input()
            
            if(curstr == ""):
                continue

            curstr = curstr.lower()

            for i in sym_to_remove:
                curstr = curstr.replace(i," ")
                
            curstr = curstr.strip()
            
            curset = set(curstr.split())

            for i in words_to_remove:
                for j in curset:
                    if(string_compare(i,j) >= 0.55):
                        tmplist.append(j)
                        
            for i in tmplist:
                curset.remove(i)

            curset = frozenset(curset)
            
            if(curset in history):
                curanswer = history[curset]
            else:
                curanswer = bool(random.randint(0,1))
                history[curset] = curanswer
                
            if(curanswer == True):
                print("Ответ: Да")
            else: # False
                print("Ответ: Нет")            
        # while True
    # try
    except KeyboardInterrupt:
        pass
    
