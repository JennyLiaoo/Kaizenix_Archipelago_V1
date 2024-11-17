from cmu_graphics import *
from PVector import PVector
class Weapon:

    def __init__(self, image, atk, range, effect):
        self.image = Image(image)
        self.effect = effect
        self.atk = atk
        self.range = range
        self.attacking = False


    def getRange(self):
        return self.range

    def drawEffect(self):
        drawImage(self.effect)
    def changeImage(self, imageIndex, possibleImages=[]):
        self.playerImage = possibleImages[imageIndex]
    def redrawAll(self):
        drawImage(self.playerImage, self.x,self.y,  width=50,height=50,align = 'center')
        if(self.attacking == True):
            drawEffect()
