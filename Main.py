from cmu_graphics import *
from PVector import PVector
from Player import Player
from Scene1 import Scene1


def onAppStart(app):
    app.player = Player(app.width/2-25, app.height/2-25)
    app.scene1 = Scene1(0,0, app.player)



def redrawAll(app):
    app.scene1.redrawAll()
    app.scene1.updatePlayer(app.player)
    app.player.redrawAll()


def onStep(app):
    checkCollisions(app)



def checkCollisions(app):
    for obs in app.scene1.obstacles:
        collide = app.player.checkCollisions(obs)
        if(collide == 'bottom'):
            app.scene1.add(0, -5)
        elif(collide == 'left'):
            app.scene1.add(5, 0)
        elif(collide == 'top'):
            app.scene1.add(0, 5)
        elif(collide == 'right'):
            app.scene1.add(-5, 0)








def onKeyHold(app, keys):
    if ('down' in keys):
        app.scene1.add(0, -5)
        app.player.changeImage(1)
        app.player.direction = 'front'
    if('up' in keys):
        app.scene1.add(0, 5)
        app.player.changeImage(0)
        app.player.direction = 'back'
    if('left' in keys):
        app.scene1.add(5, 0)
        app.player.changeImage(2)
        app.player.direction = 'left'
    if ('right' in keys):
        app.scene1.add(-5, 0)
        app.player.changeImage(3)
        app.player.direction = 'right'

def onKeyPress(app, key):
    if(key == 'space' and app.player.cooldown == False):
        app.player.hitAnimation(app.scene1.enemies)


def main():
    runApp(width=800, height=500)


main()
