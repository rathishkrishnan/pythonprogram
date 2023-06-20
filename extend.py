##a=[10,20,30,40]
##a.extend([1,2,3,4])
##print(a)
##
##a=[10,20,30]
##b=a.pop(1)
##print(b)

##a=[10,20,30]
##a.reverse()
##print(a)

#a=['a','s','']

x=0
for i in range(0,6):
    for j in range(0,6):
        if(i>=j):
            x+=1
            #x=1+i+j
            print(x,end="")
    print()        
