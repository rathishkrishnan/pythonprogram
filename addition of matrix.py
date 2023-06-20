rows=int(input("enter a rows:"))
columns=int(input("enter a columns:"))
a=[]
for i in range(rows):
    a.append([])
    for j in range(columns):
        x=int(input("enter a number:"))
        a[i].append(x)
        
print(a)

rows=int(input("enter a rows:"))
columns=int(input("enter a columns:"))
b=[]
for i in range(rows):
    b.append([])
    for j in range(columns):
        x=int(input("enter a number:"))
        b[i].append(x)
print(b)    


n=[]
for i in range(rows):
   n.append([])
    for j in range(columns):
        x=a[i][j]+b[i][j]
        n[i].append(x)
    print(x)
    
print()

