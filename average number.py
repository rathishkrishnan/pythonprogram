n=int(input("enter a number of subject:"))
a=0
for i in range(1,n+1):
    x=int(input("enter your subject mark subject:"))
    a=x+a
    b=a//n
print("the average of",n,"subject is",b)
    
