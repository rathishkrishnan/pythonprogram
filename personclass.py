
##class Person:
##    name="bruce wayne"
##    country="united kingdom"
##    dateofbirth="18-03-2006"
##    a=int(dateofbirth[-4::])
##    b=2023
##    def age(x):
##        print("the age of the person is",x.b-x.a)
##p=Person()
##p.age()
def max_end3(n):
  newList=[]
  greatestNumber=0
  firstNumber=n[0]
  lastNumber=n[-1]
  if(firstNumber>lastNumber):
    greatestNumber=firstNumber
  else:
    greatestNumber=lastNumber
    
  for i in range(len(n)):
      newList.append(greatestNumber)
  return newList


print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
