from cmu_graphics import *
from PVector import PVector
from Player import Player


def onAppStart(app):
    app.url = 'https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg'
    app.player = Player(100, 100)


def redrawAll(app):
    imageWidth, imageHeight = getImageSize(app.url)
    drawLabel(f'Original ({imageWidth}x{imageHeight})', 125, 75, size=16)
    drawImage(app.url, 125, 200, align='center')

    app.player.redrawAll()


def onKeyPress(app, key):
    if (key == 'right'):
        app.player.add(5, 0)
    elif (key == 'up'):
        app.player.add(0, -5)
    elif (key == 'left'):
        app.player.add(-5, 0)
    elif (key == 'down'):
        app.player.add(0, 5)


def main():
    runApp()


main()
