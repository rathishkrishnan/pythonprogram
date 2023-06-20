a=int(input("age of a:"))
b=int(input("age of b:"))
c=int(input("age of c:"))
if(a>b and a>c):
    print("a is older than b and c")
elif(b>a and b>c):
    print("b is older than a and c")
elif(c>a and c>b):
    print("c is older than a and b")

elif(a<b and a<c):
    print("a is younger than b and c")
elif(b<a and b<c):
    print("b is younger than a and c")
elif(c<a and c<b):
    print("c is younger than a and b")
else:
    print("all are same age")
