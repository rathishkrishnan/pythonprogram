x=0
z=[]
while True:
    n=input("enter a number:")
    a=n.isalpha()
    if(a==True):
        break
    else:
        z.append(n)
        x=x+int(n)
print("sum of the number:",x,)
print("average of the number:",x/len(z))
