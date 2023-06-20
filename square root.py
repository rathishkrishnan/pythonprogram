a=int(input("enter a number:"))
b=int(input("enter a result:"))    
count=0
while(a!=0):
    x=a**count
    count+=1
    if(x==b):
      print("the number of time the code repeated is",count-1)
    
 
