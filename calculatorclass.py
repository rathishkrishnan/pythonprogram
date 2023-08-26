
class Calculator:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    def add(x):
        print("the sum of the two numbers is",x.a+x.b)
    def sub(x):
        print("the differrence of the two numbers is",x.a-x.b)
    def mult(x):
        print("the multiplication of the two numbers is",x.a*x.b)
    def div(x):
        print("the division of the two numbers is",x.a/x.b)
c=Calculator()
c.add()
c.sub()
c.mult()
c.div()
