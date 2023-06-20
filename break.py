a=0
while(a<10):
    if(a==6):
        break
    a+=1
    print(a)
print("while loop break example")

for i in range(1,11):
    if(i==7):
        break 
    print(i)
print("for loop break example")


a=0
while(a<10):
    if(a==3):
        a+=1
        continue
    print(a)
     a+=1
print("while loop continue example")
    
    
for i in range(1,11):
    if(i==5):
        continue
    print(i)
print("for loop continue example")
