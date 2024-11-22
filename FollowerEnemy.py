from Enemy import Enemy
from cmu_graphics import *
import math
from PVector import PVector
class FollowerEnemy(Enemy):

    def __init__(self, x, y, health, size,speed):
        super().__init__(x, y, health, 10)
        self.directionSignX = 1
        self.directionSignY = 1
        self.speed = speed
        self.size = size
        self.canMove = True
        self.disX = 0
        self.disY = 0
        self.w = size
        self.h = size

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
    # checks if the player is in the follower enemy's attack range.
    def isColliding(self, other):
        if (self.x + self.size >= other.x and self.x <= other.x + other.w and self.y == other.y + other.h and almostEqual(self.y, other.y + other.h)):
            return 'bottom'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and almostEqual(self.x + self.size, other.x)):
            return 'left'
        elif (self.x + self.size >= other.x and self.x <= other.x + other.w and almostEqual(self.y + self.size, other.y)):
            return 'top'
        elif (self.y + self.size >= other.y and self.y <= other.y + other.h and almostEqual(self.x, other.x + other.w)):
            return 'right'

    def checkMove(self, other):
        if (self.isColliding(other) == 'bottom'):
            self.canMove = False
            self.disY = -1
            return True
        elif (self.isColliding(other) == 'top'):
            self.canMove = False
            self.disY = 1
            return True
        elif (self.isColliding(other) == 'left'):
            self.canMove = False
            self.disX = 1
            return True
        elif (self.isColliding(other) == 'right'):
            self.canMove = False
            self.disX = -1
            return True
        else:
            self.canMove = True
            return False


    def move(self, player):
        disX = player.x - self.x
        disY = player.y - self.y
        distance = math.sqrt((player.x - self.x) ** 2 + (player.y - self.y) ** 2)
        ratio = self.speed / distance
        disX *= ratio
        disY *= ratio
        if(self.canMove):
            self.x += disX
            self.y += disY
        else:
            # right
            if(self.disX < 0 and disY >= 0):
                self.x -= 0.1
                self.y += 0.1
            elif(self.disX < 0 and disY < 0):
                self.x -= 0.1
                self.y -= 0.1

            # bottom
            if (self.disY < 0 and disX <= 0):
                self.x -= 0.1
                self.y -= 0.1
            elif (self.disY < 0 and disX > 0):
                self.x += 0.1
                self.y -= 0.1

            # left
            if (self.disX > 0 and disY <= 0):
                self.x += 0.1
                self.y -= 0.1
            elif (self.disX > 0 and disY > 0):
                self.x += 0.1
                self.y += 0.1

            # top
            if (self.disY > 0 and disX <= 0):
                self.x -= 0.1
                self.y += 0.1
            elif (self.disY > 0 and disX > 0):
                self.x += 0.1
                self.y += 0.1


    def almostEqual(self, one, two):
        if(abs(one-two) < 2):
            return True
        else:
            return False






    # other is the object hitting the enemy
    def takeDmg(self, other):
        if(self.immunity == False):
            self.health -= other.atk

    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=self.size,height=self.size)
