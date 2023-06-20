kilometers=int(input("number of kilometers u covered:"))
if(kilometers>=1 and kilometers<=150):
    if(kilometers>=1 and kilometers<=10):
        a=kilometers*11
        print("per kilometers costs rs11 but u covered",kilometers,"km it costs rs",a)
    elif(kilometers>=11 and kilometers<=100):
        remaining_km=kilometers-10
        b=(10*11)+(remaining_km*10)
        print("per kilometers costs rs10 but u covered",kilometers,"km it costs rs",b)
    elif(kilometers>100):
        remaining_km=kilometers-100
        c=(10*11)+(90*10)+(remaining_km*9)
        print("per kilometers costs rs9 but u covered",kilometers,"km it costs rs",c)
else:
    print("invalid input")
