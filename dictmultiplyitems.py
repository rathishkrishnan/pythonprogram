d1={1:10,2:6,3:5}
d2={4:4,5:9,6:2}
x={}
a=d1.values()
b=d2.values()
c=list(a)
d=list(b)
print(c,d)
for i in range(len(c)):     
    for j in range(len(d)):
        e=c[i:j]
        f=d[i:j]
    print(e*f)
         
for i in d1.values():
    for j in d2.values():
        y=i*j
       print(y)
        #x.update({1:y})
print(x)
    

