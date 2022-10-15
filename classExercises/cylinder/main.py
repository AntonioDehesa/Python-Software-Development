class Cylinder():
    PI = 3.14
    def __init__(self, radius: int = 0, height: int = 0):
        self.radius = radius
        self.height = height

    def getVolume(self):
        return ((self.radius**2)*self.height*self.PI)

    def getSurfaceArea(self):
        return (2*self.PI*self.radius*(self.radius+self.height))

    def setHeight(self, newHeight):
        self.height = newHeight
    
    def print(self):
        print("Radius: {}, Height: {}, Volume: {}, Surface Area: {}".format(self.radius, self.height, self.getVolume(), self.getSurfaceArea()))

    
if __name__ == "__main__":
    myC = Cylinder(10,10)
    print(myC.getSurfaceArea())
    print(myC.getVolume())
    print(myC.print())
    #print(myC.PI)