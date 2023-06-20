a=['abc','xyz','aba','1221']
x=0
for i in a:
    y=len(i)-1
    z=i[0]
    n=i[y]
    if(z==n):
        x=x+1
print(x)
