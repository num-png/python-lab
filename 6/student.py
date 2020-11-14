from funcs import *

class Student:
    def __init__(self, lastname, firstname, middlename, birthyear, height, disciplines):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.birthyear = birthyear
        self.disciplines = disciplines
        self.height = height
        # Обязательные данные - Фамилия, имя. отчество, год рождения, по ним создается ключ
        self.key = (self.lastname, self.firstname, self.middlename, self.birthyear)
    def __repr__(self):
        return("Student("+
              self.lastname+", "+
              self.firstname+", "+ 
              self.middlename+", "+
               str(self.birthyear)+")")
    # поиск по фамилии, имени, отчеству
    def match_firstname(self, s):
        return (self.firstname.tolower == s.tolower)
    def match_lastname(self, s):
        return (self.lastname.tolower == s.tolower)
    def match_middlename(self, s):
        return (self.middlename.tolower == s.tolower)
    
def create_student_dict(invar):
    result = {}
    for i in invar:
        tmp = Student(i[0],i[1],i[2],
                      invar[i]['дата рождения'],
                      invar[i]['рост'],
                      invar[i]['предметы'])
        result[tmp.key] = tmp
    return result
