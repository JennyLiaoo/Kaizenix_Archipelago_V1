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

    def getX(self):
        return self.x

    def getY(self):
        return self.y