signal=input("enter your colour:")
if(signal=="red"):
    print("car has to stop")
elif(signal=="yellow"):
    print("car has to wait")
elif(signal=="green"):
    print("car allowed to go")
else:
    print(signal,"is unrecognized signal")
