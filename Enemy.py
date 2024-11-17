from cmu_graphics import *
from PVector import PVector
class Enemy:

    def __init__(self, x, y, health, range):
        self.possibleImages = ['Images/catBack1.png', 'Images/catBack2.png', 'Images/catFront1.png', 'Images/catFront2.png', 'Images/catLeft1.png',
                          'Images/catLeft2.png', 'Images/catRight1.png', 'Images/catRight2.png']
        self.health = health
        self.range = range
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.playerImage = self.possibleImages[0]
        self.immunity = False

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
    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=50,height=50,align = 'center')
