n=int(input("enter a number:"))
x=0
a=[]
b=[]
for i in range(1,n+1):
    if(n%i==0):
       a.append(i)
       for z in range(2,n):
           if(a[z]%z==0):
               print("not a prime")
               x+=1
               break
       if(x==0):
           b.append(y)
           print(b)
         
            
            
