from cmu_graphics import *
from PVector import PVector
from Weapon import Weapon
class Player:
    def __init__(self, x, y):
        self.possibleImages = [['Images/catBack1.png', 'Images/catFront1.png', 'Images/catLeft1.png', 'Images/catRight1.png'],
                               ['Images/catBack2.png', 'Images/catFront2.png', 'Images/catLeft2.png','Images/catRight2.png']]
        self.counter = 0
        self.atk = 10
        self.currentImage = self.possibleImages[0]
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.playerImage = self.currentImage[0]
        self.size = 50
        self.health = 50
        self.immunityDuration = 100
        self.immune = False
        self.cooldown = False
        self.cooldownCounter = 0
        self.cooldownDuration = 50
        self.direction = 'front'
        self.weapon = Weapon(['Images/weapon0.png', 'Images/weapon1.png', 'Images/weapon2.png', 'Images/weapon3.png'], 10, 50, 25, 15)
        self.weaponDrawn = False
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
        if(self.cooldown == True):
            self.cooldownCounter += 1
            if (self.cooldownCounter > self.cooldownDuration):
                self.cooldown = False
                self.cooldownCounter = 0
        if(self.weaponDrawn == True):
            self.weapon.redrawAll()
            if(self.weapon.drawnCounter >= self.weapon.timeAtk):
                self.weaponDrawn = False
                self.weapon.drawnCounter = 0

    def checkHit(self, other):
        pass

    def hitAnimation(self, enemies):
        # increment player animation
        self.cooldown = True
        self.weapon.changeLocation(self.direction, self.x, self.y, self.size, self.size)
        self.depleteEnemyHealth(enemies)
        self.weaponDrawn = True


    def depleteEnemyHealth(self, enemies):
        for enemy in enemies:
            if(self.weapon.checkCollisions(enemy) != None):
                enemy.health -= self.weapon.atk
                print('hit', enemy.health)





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

