from cmu_graphics import *
from PVector import PVector
from Obstacle import Obstacle
from LineEnemy import LineEnemy
from CrossEnemy import CrossEnemy
from FollowerEnemy import FollowerEnemy
class Scene1:
    def __init__(self, x, y, player):
        self.player = player
        self.x = x
        self.y = y
        self.position = PVector(self.x,self.y)
        self.background = 'Images/background.jpg'
        self.obstacles = []
        obs1 = Obstacle(100, 100, 100, 100)
        obs2 = Obstacle(300, 350, 50, 50)
        obs3 = Obstacle(0, 300, 100, 50)
        obs4 = Obstacle(0, 0, 10, 1000)
        obs5 = Obstacle(0, 500, 1000, 10)
        obs6 = Obstacle(600, 0, 10, 1000)
        obs7 = Obstacle(0, 0, 1000, 10)
        self.obstacles.append(obs1)
        self.obstacles.append(obs2)
        self.obstacles.append(obs3)
        self.obstacles.append(obs4)
        self.obstacles.append(obs5)
        self.obstacles.append(obs6)
        self.obstacles.append(obs7)
        self.enemies = []
        enemy1 = LineEnemy(10, 100, 50, 'x', 1, 50)
        #enemy2 = CrossEnemy(250, 100, 50, 'x', 5, 50)
        #enemy3 = FollowerEnemy(300, 150, 50, 50, 2)
        self.enemies.append(enemy1)
        #self.enemies.append(enemy2)
        #self.enemies.append(enemy3)


    def updatePlayer(self, player):
        self.player = player
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def add(self, xAdd, yAdd):
        self.x += xAdd
        self.y += yAdd
        for obs in self.obstacles:
            obs.add(xAdd, yAdd)
        for enemy in self.enemies:
            enemy.add(xAdd, yAdd)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def drawObstacles(self):
        for obs in self.obstacles:
            obs.redrawAll()
    def drawEnemies(self):
        for enemy in self.enemies:
            enemy.redrawAll()
    def checkMoveEnemy(self):
        for enemy in self.enemies:
            for obs in self.obstacles:
                if(enemy.checkMove(obs)):
                    break
            self.moveEnemies(enemy)

    def moveEnemies(self, enemy):
        if(type(enemy) == FollowerEnemy):
            enemy.move(self.player)
        else:
            enemy.move()



    def redrawAll(self):
        drawImage(self.background, self.x,self.y,  width=2000,height=1500,align = 'center')
        self.drawObstacles()
        self.checkMoveEnemy()
        self.drawEnemies()
