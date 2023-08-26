##a=[10,15,23,20,44,56]
##b=[]
##for i in a:
##    if(i%2==0):
##       b.append(i)
## print(b)    

a=[10,20,15,23,44,56]
def even(n):
    return(n%2==0)
x=list(filter(even,a))
print(x)

import functools
a=[10,15,20,25,28]
def add (a,b):
    print("a=",a,"b=",b)
    return a+b
x=functools.reduce(add,a) 
print(x)


 
