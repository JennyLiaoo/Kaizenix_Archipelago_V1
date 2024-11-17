from cmu_graphics import *
from PVector import PVector
class Player:
    def __init__(self, x, y):
        self.possibleImages = [['Images/catBack1.png', 'Images/catFront1.png', 'Images/catLeft1.png', 'Images/catRight1.png'],
                               ['Images/catBack2.png', 'Images/catFront2.png', 'Images/catLeft2.png','Images/catRight2.png']]
        self.counter = 0
        self.currentImage = self.possibleImages[0]
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.playerImage = self.currentImage[0]
        self.size = 50
        self.health = 50
        self.immunityDuration = 100
        self.immune = False

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
    def changeImage(self, imageIndex):
        self.playerImage = self.currentImage[imageIndex]
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=self.size,height=self.size)
        if(self.counter%5==0 and self.counter < 10):
            self.currentImage = self.possibleImages[0]
        elif(self.counter%10==0):
            self.currentImage = self.possibleImages[1]
            self.counter = 0
        self.counter = self.counter+1

    def checkHit(self, other):
        pass

    def hitBackAnimation(self):
        pass

    def checkCollisions(self, other):
        if(self.x + self.size >= other.x and self.x <= other.x+other.w and self.y == other.y + other.h and self.y == other.y + other.h):
            return 'bottom'
        elif(self.y + self.size >= other.y and self.y <= other.y + other.h and self.x + self.size == other.x):
            return 'left'
        elif (self.x + self.size >= other.x and self.x <= other.x + other.w and self.y + self.size == other.y):
            return 'top'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and self.x == other.x + other.w):
            return 'right'

