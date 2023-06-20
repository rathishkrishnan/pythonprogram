prime=int(input("enter the number:"))
a=0
for i in range(2,prime):
    if(prime%2==0):
        print("the given number is not a prime number")
        a+=1
        break
else:
    print("the given number is  a prime number")

