from cmu_graphics import *
from PVector import PVector
class Weapon:

    def __init__(self, images, atk, width, height, timeAtk):
        self.images = images
        self.image =images[0]
        self.atk = atk
        self.height = height
        self.width = width
        self.imageWidth = width
        self.imageHeight = height
        self.attacking = False
        self.drawn = False
        self.drawnCounter = 0
        self.timeAtk = timeAtk
        self.x, self.y = None, None



    def getRange(self):
        return (self.range, self.width)

    def drawEffect(self):
        drawImage(self.effect)
    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]
    def changeLocation(self, playerDirection, playerX, playerY, playerWidth, playerHeight):
        if(playerDirection == 'front'):
            self.image =self.images[2]
            self.x = playerX
            self.y = playerY+playerHeight
            self.imageWidth = self.width
            self.imageHeight = self.height
        elif (playerDirection == 'back'):
            self.image = self.images[0]
            self.x = playerX
            self.y = playerY - self.height
            self.imageWidth = self.width
            self.imageHeight = self.height
        elif (playerDirection == 'left'):
            self.image = self.images[3]
            self.x = playerX - self.height
            self.y = playerY
            self.imageWidth = self.height
            self.imageHeight = self.width
        elif (playerDirection == 'right'):
            self.image = self.images[1]
            self.x = playerX+playerWidth
            self.y = playerY
            self.imageWidth = self.height
            self.imageHeight = self.width


    def redrawAll(self):
        drawImage(self.image, self.x, self.y, width=self.imageWidth, height=self.imageHeight)
        self.drawnCounter+=1

    def checkCollisions(self, other):
        r1 = (self.x, self.y, self.x+self.imageWidth, self.y+self.imageHeight)

        r2 = (other.x, other.y , other.x + other.w, other.y+ other.h)
        if(r1[2] <= r2[0] or r2[2] <= r1[0]):
            print('reach1')
            return None
        if(r1[3]<=r2[1] or r2[3]<=r1[1]):
            print('reach2')
            return None
        print('reach3')
        return 1
