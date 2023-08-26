class Bike:
    brand="yamaha"
    model="R15 V3"
    typeofengine=6
    gears=6
    tankcapacity=3
    mileage=70
    colour="black"
    maxspeed=250
    def travel(self):
        print(self.model)
    def setproperty(self,b,m,t,g,tc,ml,c,mx):
        self.brand=b
        self.model=m
        self.typeofengine=t
        self.gears=g
        self.tankcapacity=tc
        self.mileage=ml
        self.colour=c
        self.maxspeed=mx
    def display(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("type of engine:",self.typeofengine)
        print("gears:",self.gears)
        print("tankcapacity:",self.tankcapacity)
        print("mileage:",self.mileage)
        print("colour:",self.colour)
        print("maxspeed:",self.maxspeed)
b=Bike()
b.display()
b.setproperty("yamaha","R15 V4",6,6,4,60,"dark blue",260)
b.display()
##b1=Bike()
##b1.display()
