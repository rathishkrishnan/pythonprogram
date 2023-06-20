eng=int(input("enter your english mark:"))
math=int(input("enter your maths mark:"))
science=int(input("enter your science mark:"))
social=int(input("enter your social mark:"))
if(eng>=35 and math>=35 and science>=35 and social>=35):
    if(eng>80 and math>80 and science>80 and social>80):
        print("science stream is alloted for u")
    elif(eng>80 and math>50 and social>=35 and science>50):
        print("commerce stream is alloted for u")
    elif(eng>80 and social>80 and math>=35 and science>35):
        print("humanities stream is alloted for u")
else:
    print("invalid input")
