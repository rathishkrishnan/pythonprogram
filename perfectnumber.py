n=int(input("enter a number:"))
a=0
for i in range(1,n):
    if(n%i==0):
        a=a+i
if(n==a):
    print(a)
    print("perfect number")
else:
    print("not a perfect number")
           
