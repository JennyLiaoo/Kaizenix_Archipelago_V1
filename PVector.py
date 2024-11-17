import math
class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd
    def mult(self, multiplier):
        self.x *= multiplier
        self.y*= multiplier
    def getSize(self):
        return abs(math.sqrt(self.x*self.x+self.y*self.y))
    def setSize(self, s):
        currentSize = self.getSize()
        if(currentSize == 0):
            self.setPos(s, 0)
        else:
            self.mult(1/currentSize)
            self.mult(s)
    def getAngle(self):
        return math.atan2(self.y, self.x)

    def setAngle(self, angle):
        size = self.getSize()
        while(angle <= 0):
            temp = abs(angle)
            angle = 360-temp
        while(angle >= 360):
            angle -= 360
        angleInRad = math.radians(angle)
        if(angle >= 0 and angle < 90):
            x = abs(size*math.cos(angleInRad))
            y = abs(size*math.sin(angleInRad))
        elif (angle >= 90 and angle < 180):
            x = -abs(size * math.cos(angleInRad))
            y = abs(size * math.sin(angleInRad))
        if (angle >= 180 and angle < 270):
            x = -abs(size * math.cos(angleInRad))
            y = -abs(size * math.sin(angleInRad))
        if (angle >= 270 and angle < 360):
            x = abs(size * math.cos(angleInRad))
            y = -abs(size * math.sin(angleInRad))

    def getX(self):
        return self.x

    def getY(self):
        return self.y