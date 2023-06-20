num=int(input("enter your number:"))
while(num<1000):
    a=num%10
    b=(num%100)//10
    c=(num%1000)//100
    print("the seperated number is",a,b,c)
    break

     
