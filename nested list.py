rows=int(input("enter a rows:"))
columns=int(input("enter a columns:"))
a=[]
for i in range(rows):
    a.append([])
    for j in range(columns):
        x=int(input("enter a number:"))
        a[i].append(x)
print(a)    
   

