age=int(input("enter your age:"))
gender=input("enter your gender:")
days=int(input("number of days:"))
if(age>=18 and age<=60 and (gender=="M" or gender=="F")):
   if(age>=18 and age<30 and gender=="M"):
      print(" your wages per day is 700 but your wages",days,"days is",days*700)
   elif(age>=18 and age<30 and gender=="F"):
      print("your wages per day is 750 but your wages",days,"days is",days*750)
   elif(age>=30 and age<=40 and gender=="M"):
      print("your wages per day is 800 but your wages",days,"days is",days*800)
   elif(age>=18 and age<=40 and gender=="F"):
      print("your wages per day is 850 but your wages",days,"days is",days*850)
else:
    print("invalid age")
