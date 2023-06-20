a=int(input("enter your angle 1:"))
b=int(input("enter your angle 2:"))
c=int(input("enter your angle 3:"))
if(a==b and b==c and c==a):
    print("it is equilateral triangle")
elif(a==b or b==c or c==a):
    print("it is isoceles triangle")
elif(a!=b and b!=c and c!=a):
    print("it is scalene triangle")
