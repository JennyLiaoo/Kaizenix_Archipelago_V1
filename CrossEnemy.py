from LineEnemy import LineEnemy
from cmu_graphics import *
import random
from PVector import PVector
class CrossEnemy(LineEnemy):
    def __init__(self, x, y, health, direction, speed,size):
        super().__init__(x, y, health, direction, speed,size)
        self.direction = direction
        self.directionSign = 1
        self.speed = speed
        self.size = size
        self.w = size
        self.h = size

    # moves the enemy towards the player, where other is the object we are moving towards
    def checkMove(self, other):
        collided = False
        if (self.isColliding(other) == 'bottom'):
            self.y+=self.speed
            collided = True
        elif (self.isColliding(other) == 'top'):
            self.y-=self.speed
            collided = True
        elif (self.isColliding(other) == 'left'):
            self.x -= self.speed
            collided = True
        elif (self.isColliding(other) == 'right'):
            self.x+=self.speed
            collided = True
        if(collided):
            self.directionSign, self.direction = self.randomize(self.directionSign, self.direction)

    def randomize(self, oldDirectionSign, oldDirection):
        diceRoll1 = random.randrange(0, 2)
        diceRoll2 = random.randrange(0, 2)
        if(diceRoll1 == 0):
            directionSign = 1
        else:
            directionSign = -1
        if(diceRoll2 == 0):
            direction = 'x'
        else:
            direction = 'y'
        if((directionSign, direction) == (oldDirectionSign, oldDirection)):
            return self.randomize(oldDirectionSign, oldDirection)
        else:
            return directionSign, direction






