s1=int(input("enter your side 1:"))
s2=int(input("enter your side 2:"))
s3=int(input("enter your side 3:"))
if(s1+s2>s3 or s2+s3>s1 or s3+s1>s2):
    print("the given sides can form a triangle")
else:
    print("the given sides cannot form a triangle")
