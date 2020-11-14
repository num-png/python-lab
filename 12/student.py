import random
from funcs import *

# Данный класс идентифицирует человека, по мало или редкоизменяющимся аттрибутам.
# Фамилия, имя, отчество, год рождения, рост (после какого-то момента, человек все же прекращает сильно расти).
class Human:    
    def __init__(self, lastname, firstname, middlename, birthyear, height):
        self.lastname = str(lastname)
        self.firstname = str(firstname)
        self.middlename = str(middlename)
        self.birthyear = int(birthyear)
        self.height = float(height)
        self.key = (self.lastname, self.firstname, self.middlename, self.birthyear)
    def __repr__(self):
        return("Human("+
               self.lastname+", "+
               self.firstname+", "+ 
               self.middlename+", "+
               str(self.birthyear)+")")

# Дисциплина
class Discipline:
    def __init__(self, name, mark):
        self.name = str(name)
        self.mark = float(mark)
        self.key = str(name)
    def __repr__(self):
        return("Discipline("+self.name+", "+str(self.mark)+")")

# У студента есть список дисциплин
class Student:
    def __init__(self, identity, disciplines):
        self.identity = identity
        self.disciplines = disciplines
        self.key = identity.key
        self.__initialfreeactions__ = 3 # свободные действия
        self.freeactions = self.__initialfreeactions__ # свободные действия
    def __repr__(self):
        return("Student("+
               str(self.identity) + ", " + str(self.disciplines)+")")
    def list_disciplines(self):
        result = []
        
        for i in self.disciplines:
            result.append([i,self.disciplines[i].mark])
            
        return result
    #def
    # действия
    # учить случайные дисциплины
    def study(self):
        tmplist = list(self.disciplines)
        
        while (self.freeactions > 0):
            randnum = random.randint(0,len(tmplist)-1)
            self.freeactions -= 1
            self.disciplines[tmplist[randnum]].mark += random.random()*0.2
            self.disciplines[tmplist[randnum]].mark = round(self.disciplines[tmplist[randnum]].mark,2)
            if(self.disciplines[tmplist[randnum]].mark > 5) :
                self.disciplines[tmplist[randnum]].mark = 5
            
        return
    # отдохнуть - восстановить силы
    def rest(self):
        self.freeactions = 3
        
        for i in self.disciplines:
            self.disciplines[i].mark -= round(random.random()*0.1,2)
            self.disciplines[i].mark = round(self.disciplines[i].mark,2)
            if(self.disciplines[i].mark < 0):
                self.disciplines[i].mark = 0
        return

def students_disciplines_fromdict(invar):
    result = {}
    for i in invar:
        name = i
        mark = invar[i]
        tmp = Discipline(name,mark)
        result[tmp.key] = tmp
        
    return result

def students_fromdict(invar):
    result = {}
    for i in invar:
        tmp_human = Human(i[0],i[1],i[2],invar[i]['дата рождения'],invar[i]['рост'])
        tmp_student = Student(tmp_human,
                      students_disciplines_fromdict(invar[i]['дисциплины']))
        result[tmp_student.key] = tmp_student
    return result

def students_study(invar):
    for i in invar:
        invar[i].study()
    return

def students_rest(invar):
    for i in invar:
        invar[i].rest()
    return

def students_print_disciplines(invar):
    for i in invar:
        print(str(i)+": "+str(invar[i]))
