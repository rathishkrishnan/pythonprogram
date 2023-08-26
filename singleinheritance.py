class RefillPen:
    def __init__(self,brand,Refillcapacity,colour):
       self.brand=brand
       self.Refillcapacity=Refillcapacity
       self.colour=colour
    def writing(self):
        print("you can write by using",self.brand,"pen")
class FountainPen(RefillPen):
    def __init__(self,brand,Refillcapacity,colour,inkconveter, nib):
        super().__init__(brand,Refillcapacity,colour)
        self.inkconveter=inkconveter
        self.nib=nib
    def capacity(self):
        print("you can fill the ink many times in",self.brand)
    def display(self):
        print("brand",self.brand)
        print("refillcapacity",self.Refillcapacity)
        print("colour",self.colour)
        print("inkconveter",self.inkconveter)
        print("nib",self.nib)
r=FountainPen("butterfly",5,"blue",1,2)        
r.display()
r.writing()
r.capacity()
        
