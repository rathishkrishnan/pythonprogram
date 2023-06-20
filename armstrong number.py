num=int(input("enter a number:"))
x=0
b=num
while(num>0):
    a=(num%10)
    num=num//10
    a=a**3
    x=x+a
print(x)
if(b==x):
    print("the given number is armstrong number")
else:
    print("the given number is not a armstrong number")
    
 
  
