salary=int(input("enter your salary:"))
years=int(input("enter your year of experience:"))
if(years>10):
    bonus=10/100*salary
    print("bonus of your working expericence is",bonus,"finally your current salary is",salary+bonus)
elif(years>=6 and years<=10):
    bonus=8/100*salary
    print("bonus of your working expericence is",bonus,"finally your current salary is",salary+bonus)
elif(years<6):
    bonus=5/100*salary
    print("bonus of your working expericence is",bonus,"finally your current salary is",salary+bonus)
else:
    print("invalid input")
    
