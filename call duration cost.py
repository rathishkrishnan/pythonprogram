time=input("enter the time:")
day=input("enter a day:")
duration=input("enter the call duration:")
a=int(duration[0:2])*60
b=int(duration[3:])
x=a+b
y=int(time[0:2]) 
if(day=="MO"or day=="TU"or day=="WE"or day=="TH"or day=="FR"):
   if(y>7 or y<18):
        print("the cost of call duration is",x*1.25)
   elif(y>18 and y<19):
        print("the cost of call duration is",x*1.15)
elif(day=="SA" or day=="su"):
    
    print("the cost of a call duration  is",x*1.15)
