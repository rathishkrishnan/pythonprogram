import random

while True:
    a=(random.randrange(1,6))
    n=int(input("enter a number:"))
    if(n>=1 and n<=5):
        if(n==a):
            print("you won the game")

            break
        else:
            print("you lose the game")
    

