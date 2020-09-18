from random import random

def getRandomColor():
    c = hou.Color()
    c.setHSL((random() * 360, random() / 2 + .5, random() * .8 + .1))
    return c

color = False
if kwargs['shiftclick']:
    color = getRandomColor()

for node in hou.selectedNodes():
    if color:
        node.setColor(color)
    else:
        node.setColor(getRandomColor())
