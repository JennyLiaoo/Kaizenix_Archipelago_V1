from cmu_graphics import *
from PVector import PVector
class Obstacle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.w = w
        self.h = h
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def add(self, x, y):
        self.x += x
        self.y += y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    def getW(self):
        return self.w
    def getH(self):
        return self.h

    def redrawAll(self):
        drawRect(self.x,self.y, self.w, self.h, fill = 'black')


