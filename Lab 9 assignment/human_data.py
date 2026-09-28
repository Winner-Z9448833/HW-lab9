class Person:
    def __init__ (self,name,locate,weight,height):
        self.name=name
        self.locate=locate
        self.weight=weight
        self.height=height
    def show(self):
        return [self.name,self.locate,self.weight,self.height]
    def getBMI(self):
        bmi=self.weight/((self.height/100)**2)
        return bmi
        
class Student(Person):
    def __init__(self,name,locate,weight,height,stu_id,course,gpa):
        super().__init__ (name,locate,weight,height)
        self.stu_id=stu_id
        self.course=course
        self.gpa=gpa
    def show(self):
        return [self.stu_id,self.course,self.gpa,super().getBMI()]+super().show()
    
class Employee(Person):
    def __init__(self,name,locate,weight,height,emp_id,department,salary):
        super().__init__ (name,locate,weight,height)
        self.emp_id=emp_id
        self.department=department
        self.salary=salary
    def show(self):
        return [self.emp_id,self.department,self.salary,super().getBMI()]+super().show()

def person_choose(st,em):
    while True:
        try:
            p=input('student or employee:\t')
            if p=='student':
                print(f'Name:\t\t{st[4]}\nlive in:\t{st[5]}\nWeight:\t\t{st[6]}\nHeight\t\t{st[7]}')
                print(f'student id:\t{st[0]}\ncourse:\t{st[1]}\nGPA:\t\t{st[2]}')
                print(f'BMI:\t{st[3]}')
            elif p=='employee':
                print(f'Name:\t\t{em[4]}\nlive in:\t{em[5]}\nWeight:\t\t{em[6]}\nHeight\t\t{em[7]}')
                print(f'Employee id:\t{em[0]}\nDepartment:\t{em[1]}\nSalary:\t\t{em[2]}')
                print(f'BMI:\t{em[3]}')
            else:
                print('***student or employee only***')
        except Exception as e:
            print(f'{e}\n***pls try again***')
        
    
s=Student('Charlie','Dagestan',98,160,'6901012200453','Cpr.E',3.5)
e=Employee('Durahan','India',67,170,'12345678','no job',0)
person_choose(s.show(),e.show())