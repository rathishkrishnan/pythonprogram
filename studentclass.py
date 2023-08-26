class Student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def setproperty(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def display(self):
         print("name",self.name)
         print("age",self.age)
         print("maark",self.mark)
s=Student("messi",37,560)
s.display()

 
