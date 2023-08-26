def search(a):
    x=int(input('enter a number:'))
    b=a.index(x)
    print(b)
    if(x==a[0:4]):
        print(b)
    elif(x!=a[0:4]):
        print("-1")
search([1,2,3,4])
