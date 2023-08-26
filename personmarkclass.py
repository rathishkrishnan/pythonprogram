class Person:
    def __init__(self,name,age):
        self._name=name
        self.age=age
    def displayproperty(self):
        print(f"personname:{self.__name}\nage={self.age}")
class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.__mark=mark
    def getmark(self):
        return self.__mark
    def setmark(self,mark):
        self.__mark=mark
    def displayproperty(self):
        print(f"student name:{self._name}\nage={self.age}\nmark={self.__mark}")
s=Student("r",17,450)
s.displayproperty()
print(s._name)
