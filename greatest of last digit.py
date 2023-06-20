a=122
b=678
c=989
x=a%10
y=b%10
z=c%10
if(x>y and x>z):
    print("the largest last digit number is",a)
elif(y>x and y>z):
    print("the largest last digit number is",b)
elif(z>x and z>y):
    print("the largest last digit number is",c)
else:
    print("all last numbers are same")
