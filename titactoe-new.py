from turtle import *
from tkinter import *
from math import *
l = 50
#ht()

squareLocations = [[-l, l], []]
name[squareLocations][0]
win = False
def lineto(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)
    
def boardCreate():
    lineto(-0.5 * l, 1.5 * l, -0.5 * l, -1.5 * l)
    lineto(0.5 * l, 1.5 * l, 0.5 * l, -1.5 * l)
    lineto(-1.5 * l, -0.5 * l, 1.5 * l, -0.5 * l)
    lineto(1.5 * l, 0.5 * l, -1.5 * l, 0.5 * l)
def centerFinder():
    
def reigonFinder(x,y):
    penup()
    if x < -l / 2:
        if y > l / 2:
            return 0
        elif y < -l / 2:
            return 6
        else:
            return 3
    elif x > l / 2:
        if y > l / 2:
            return 2
        elif y < -l / 2:
            return 8
        else:
            return 5
    else:
        if y > l / 2:
            return 1
        elif y < -l / 2:
            return 7
        else:
            return 4
    
    
    

def clickLocation(x,y):
    goto(x,y)
    reigon = reigonFinder(x,y)
def checkReigon():
    




boardCreate()
penup()
goto(0,0)


onscreenclick(clickLocation)




  
        

