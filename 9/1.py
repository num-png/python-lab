#!/usr/bin/python

import random

if __name__ == "__main__":
    curanswer = None
    curstr = None
    
    try:
        while True:
            print("---")
            print("Введите вопрос:")
            
            curstr = input()
            if(curstr == ""):
                continue

            curanswer = bool(random.randint(0,1))

            if(curanswer == True):
                print("Ответ: Да")
            else: # False
                print("Ответ: Нет")            
        # while True
    # try
    except KeyboardInterrupt:
        pass
    
