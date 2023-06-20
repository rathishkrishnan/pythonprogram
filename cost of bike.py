cost=int(input("enter your bike price:"))
if(cost>50000 and cost>100000):
    if(cost>100000):
        print("cost of a bike when 15% of tax included is",cost-15/100*cost)
    elif(cost>50000 and cost<=100000):
        print("cost of a bike when 10% of tax included is",cost-10/100*cost)
    elif(cost<=50000):
        print("cost of a bike when 5% of tax included is",cost-5/100*cost)
else:
    print("invalid input")
