age=int(input("enter your age:"))
if(age>0 and age<=100):
    if(age>=18):
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote")
else:
    print("invalid input")
