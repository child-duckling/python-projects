from turtle import *
from tkinter import *
from math import *

#Setup
l = 25
ht()
speed(0)
p = 1
regions = {0:"nA", 1:"nA", 2:"nA", 3:"nA", 4:"nA", 5:"nA", 6:"nA", 7:"nA", 8:"nA"}
squareCenter = [
    [ -l ,l - (l / 2) ],
    [ 0 , l - (l / 2) ],
    [ l, l - (l / 2)],
    [ -l,0 - (l / 2)],
    [0, 0 - (l / 2)],
    [l, 0 - (l / 2)],
    [-l, -l - (l / 2)],
    [0, -l - (l / 2)],
    [l, -l - (l / 2)]]
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
    else:
        print("Not on the board! \n ")
        onscreenclick(clickLocation)
        return None
    
    

def clickLocation(x,y):
    goto(x,y)
    reigon = reigonFinder(x,y)
    if reigon == None:
        onscreenclick(clickLocation)
    else:
        print(reigon)
        print(squareCenter[reigon])
        if p  == 1:
            drawX(squareCenter[reigon])
            regions.update(reigon="X")
            
        else:
            drawO(squareCenter[reigon])
            reigons.update(reigon="O")

def drawO(square):
    goto(square)
    pendown()
    circle(l / 2)
    penup()
    
def drawX(square):
    goto(square)
    seth(90)
    fd( l / 2)
    pendown()
    rt(45)
    fd( l / 2)
    bk( l / 2)
    rt(90)
    fd( l / 2)
    bk( l / 2)
    rt(90)
    fd( l / 2)
    bk( l / 2)
    rt(90)
    fd( l / 2)
    bk( l / 2)
    penup()
    

#def game():




    



boardCreate()
penup()
goto(0,0)
onscreenclick(clickLocation)




  
        

