class Person:


    def __init__(self,name,l_name):
        self.name = name
        self.name = l_name

    def salary_calculate(self):
        if type(self) is Professor:
            self.total = self.salary*self.hour
            return f'{self.name}{self.l_name} salary is {self.total}'
        elif type(self) is Student:
            return f'{self.name'}{self.l_name} is a student'

class Professor(Person):   
    def __init__(self,name,l_name,posotion,salary,hour=200):
        super().__init__(name,l_name)
        self.position = position
        self.salary = salary
        self.hour = hour

class Student(Person):
    def __init__(self,name,l_name,year,field):
        super().__init__(name,l_name)
        self.year = year
        self.field = field
        


m = Professor('mahan','kabir','full-professor',500)
print(m.salary_caculate())
mo = Student('mobin','ziyaee',2,'software engineering') 
print(mo.salary_calculate())       




    