##class Greaterthan100error(Exception):
##    def __init__(self,value):
##        print("Greaterthan100error:the given value is",value)
##a=int(input("enter a number:"))
##try:
##    if(a>100):
##       raise Greaterthan100error(a)
##    else:
##       print("a is less than 100")
##        
##except:
##    print("error occured")


class EvenError(Exception):
    def __init__(self,x):
        print("EvenError:the given number is",x)
a=int(input("enter a number:"))
try:
    if(a%2==0):
       raise EvenError(a)
    else:
       print("the given number is odd")
except:
    print("Error Occured")
