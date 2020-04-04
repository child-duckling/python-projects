from turtle import *
from tkinter import *
from math import *
l = 50
#ht()













p = ""
regions = {0:"nA", 1:"nA", 2:"nA", 3:"nA", 4:"nA", 5:"nA", 6:"nA", 7:"nA", 8:"nA"}
squareLocations = [[-l, l], []]
#name[squareLocations][0]
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
#def centerFinder():
    
def reigonFinder(x,y):
    penup()
    if x < -l / 2 and x > -l / 2 - l :
        if y > l / 2 and y < l / 2 + l:
            return 0
        elif y < -l / 2 and y > -l / 2 - l:
            return 6
        elif y > -l/2 and y < l / 2:
            return 3
    elif x > l / 2 and x < l / 2 + l:
        if y > l / 2 and y < l / 2 + l:
            return 2
        elif y < -l / 2 and y > -l / 2 - l:
            return 8
        elif y > -l/2 and y < l / 2:
            return 5
    elif x < l/2 and x > -l/2:
        if y > l / 2 and y < l / 2 + l:
            return 1
        elif y < -l / 2 and y > -l / 2 - l:
            return 7
        elif y > -l/2 and y < l / 2:
            return 4
    
    
    

def clickLocation(x,y):
    goto(x,y)
    reigon = reigonFinder(x,y)
    #print(reigon)
    checkReigon(reigon)
def checkReigon(a):
    if regions[a] == '':
        regions[a] = "x"
        print( regions )
    




boardCreate()
penup()
goto(0,0)


onscreenclick(clickLocation)




  
        

