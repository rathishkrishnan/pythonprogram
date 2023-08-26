n=int(input("enter a number:"))
x={}
for i in range(n):
    a=int(input("enter a key:"))
    for j in range(1):
        b=input("enter a value:")
        x.update({a:b})
print(x)
