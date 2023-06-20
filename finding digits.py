#program to check wheather the given number is single digit or double pr triple digit
num=int(input("enter a number:"))
if(num>=0 and num<10):
    print("the given number",num,"is single digit")
elif(num>=10 and num<100):
    print("the given number",num,"is double digit")
elif(num>=100 and num<1000):
    print("the given number",num,"is three digit")
else:
    print("the given number",num,"is more than three digit")
