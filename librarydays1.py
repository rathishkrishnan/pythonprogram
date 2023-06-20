days=int(input("number of days:"))
if(days>=1 and days<=30):
    if(days>=1 and days<=5):
        a=days*2
        print("charge of per day is rs2 and charge of",days," days is",a)
    elif(days>=6 and days<=10):
        rdays=days-5
        b=(5*2)+(rdays*3)
        print("charge of per day is rs3 and charge of",days,"days is",b)
    elif(days>=11 and days<=15):
        rdays=days-10
        c=(5*2)+(5*3)+(rdays*4)
        print("charge of per day is rs4 and charge of",days,"days is",c)
    elif(days>15):
        rdays=days-15
        d=(5*2)+(5*3)+(5*4)+(rdays*5)
        print("charge of per day is rs5 and charge of",days,"days is",d)
else:
    print("more than 30 days are not applicable")
        
