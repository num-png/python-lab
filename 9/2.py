#!/usr/bin/python

import random
from string_functions import *

if __name__ == "__main__":
    history = {}
    
    try:
        while True:
            curanswer = None
            curstr = None
            
            print("---")
            print("Введите вопрос:")
            
            curstr = input()
            curstr = curstr.lower()
                        
            if(curstr == ""):
                continue
            
            if(curstr in history):
                curanswer = history[curstr]
            else:
                curanswer = bool(random.randint(0,1))
                history[curstr] = curanswer
                
            if(curanswer == True):
                print("Ответ: Да")
            else: # False
                print("Ответ: Нет")            
        # while True
    # try
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    
