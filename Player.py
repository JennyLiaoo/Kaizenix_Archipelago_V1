from cmu_graphics import *
from PVector import PVector
class Player:

    def __init__(self, x, y):
        self.possibleImages = ['catBack1.png', 'catBack2.png', 'catFront1.png', 'catFront2.png', 'catLeft1.png',
                          'catLeft2.png', 'catRight1.png', 'catRight2.png']
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.playerImage = self.possibleImages[0]

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
        drawImage(self.playerImage, 100,100)
