from Enemy import Enemy
from cmu_graphics import *
from PVector import PVector
class LineEnemy(Enemy):
    def __init__(self, x, y, health, direction, speed,size):
        super().__init__(x, y, health, 10)
        self.direction = direction
        self.directionSign = 1
        self.speed = speed
        self.size = size
        self.w = size
        self.h = size
    def checkHit(self):
        pass

    # moves the enemy towards the player, where other is the object we are moving towards
    def checkMove(self, other):
        if (self.isColliding(other) == 'bottom'):
            self.y+=self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'top'):
            self.y-=self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'left'):
            self.x -= self.speed
            self.directionSign = -self.directionSign
        elif (self.isColliding(other) == 'right'):
            self.x+=self.speed
            self.directionSign = -self.directionSign
    def move(self):
        if(self.direction == 'x'):
            self.x+=self.directionSign * self.speed
        else:
            self.y+= self.directionSign * self.speed

    def isColliding(self, other):
        if (self.x + self.size >= other.x and self.x <= other.x + other.w and self.y == other.y + other.h and self.y == other.y + other.h):
            return 'bottom'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and self.x + self.size == other.x):
            return 'left'
        elif (self.x + self.size >= other.x and self.x <= other.x + other.w and self.y + self.size == other.y):
            return 'top'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and self.x == other.x + other.w):
            return 'right'
    def hitBack(self):
        pass

    # other is the object hitting the enemy
    def takeDmg(self, other):
        if(self.immunity == False):
            self.health -= other.atk

    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=50,height=50)
