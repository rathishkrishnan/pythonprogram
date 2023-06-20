a=int(input("number of classes held:"))
b=int(input("number of classes attented:"))
percentage=b/a*100
if(percentage>75):
    print("student is allowed to sit in exam his attendence percentage is",percentage)
else:
    print("student is not allowed to sit in exam his attendence percentage is",percentage)
