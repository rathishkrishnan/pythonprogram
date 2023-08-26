def mult(n):
    if(n==1):
        return 1
    else:
        return n*mult(n-1)
n=int(input("enter a number:"))
print('the product of the n number is',mult(n))
