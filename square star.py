def squarestar():
    for i in range(5):
        for j in range(5):
            if(i*j==2 or i*j==6):
                print(" ",end='')
            else:
                 print("*",end='')
        print()
squarestar()    
