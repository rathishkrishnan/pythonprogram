class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayproperty(self):
        print(f"personname:{self.name}\nage={self.age}")
class Student(Person):
    def __init__(self,name,age,mark):
        Person.__init__(self,name,age)
        self.mark=mark
    def getmark(self):
        return self.mark
    def setmark(self,mark):
        self.mark=mark
    def displayproperty(self):
        print(f"student name:{self.name}\nage={self.age}\nmark={self.mark}")
class Teacher(Student):
    def __init__(self,name,age,mark,Class,group):
        Student.__init__(self,name,age,mark)
        self.Class=Class
        self.group=group
    def displayproperty(self):
        print(f"student name:{self.name}\nage={self.age}\nmark={self.mark}\nClass={self.Class}\ngroup={self.group}")
        
s=Teacher("r",17,450,12,"CS")
s.displayproperty()
        
