from turtle import *
from tkinter import *
from math import *
l = 50
#ht()

region = [ 11 , 12 , 13 , 21 , 22 , 23 , 31 , 32 , 33 ]


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

def reigonFinder(x,y,z):
    penup()
    goto(x,y)
    setx(x + (l /2))
    sety(x + (l /2))
    topRight = pos()
    goto(x,y)
    setx(x - (l /2))
    sety(x - (l /2))
    bottomLeft = pos()
    if z == "tr":
        return topRight
    else:
        return bottomLeft
boardCreate()
penup()
goto(0,0)


a1t = reigonFinder(-l , l,"tr")
a1b = reigonFinder(-l , l,"bl")

b1t = reigonFinder(0 , 0 + l,"tr")
b1b = reigonFinder(0 , 0 + l,"bl")

c1t = reigonFinder(l , l,"tr")
c1b = reigonFinder(l  , l ,"bl")



print(a1t)
print(a1b)
print(b1t)
print(b1b)
print(c1t)
print(c1b)
