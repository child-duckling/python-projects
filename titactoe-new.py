from turtle import *
from tkinter import *
from math import *

#Setup
l = 25
ht()
speed(0)
person = True #True - x ; False - o
regions = {10:"nA", 11:"nA", 12:"nA", 20:"nA", 21:"nA", 22:"nA", 30:"nA", 31:"nA", 32:"nA"}
squareCenter =[
    ( -l ,l - (l / 2) ),
    ( 0 , l - (l / 2) ),
    ( l, l - (l / 2)),
    ( -l,0 - (l / 2)),
    (0, 0 - (l / 2)), 
    (l, 0 - (l / 2)),
    (-l, -l - (l / 2)),
    (0, -l - (l / 2)),
    (l, -l - (l / 2))
    ]
rowcol = [10,11,12,20,21,22,30,31,32]
win = False
info = 0, 0 - l * 5
#isFirstMove = True


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
            return 10
        elif y < -l / 2 and y > -l / 2 - l:
            return 30
        elif y > -l/2 and y < l / 2:
            return 20
    elif x > l / 2 and x < l / 2 + l:
        if y > l / 2 and y < l / 2 + l:
            return 12
        elif y < -l / 2 and y > -l / 2 - l:
            return 32
        elif y > -l/2 and y < l / 2:
            return 22
    elif x < l/2 and x > -l/2:
        if y > l / 2 and y < l / 2 + l:
            return 11
        elif y < -l / 2 and y > -l / 2 - l:
            return 31
        elif y > -l/2 and y < l / 2:
            return 41
    else:
        print("Not on the board! \n ")
        onscreenclick(clickLocation)
        return None
    
    

def clickLocation(x,y):
    global regions
    global person
    
    goto(x,y)
    region = reigonFinder(x,y)
    if region != None:
        #print(region)
        #print(squareCenter[region])
        checkBoard(regions)
        if  checkReigon(region) = True:
            return
            if person == True:
                drawX(squareCenter[region])
                regions.update(region="X")
            else:
                drawO(squareCenter[region])
                regions.update(region="O")
            person = not person

    else:
        print("Try again!")
    checkBoard()

def drawO(square):
    goto(square)
    sety(ycor() + l / 1.125)
    setx(xcor() + l / 2.9)
    pendown()
    circle(l / 2.5)
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
    
def printInfo(t):
    penup()
    goto(info)
    pendown()
    write(t)
    penup()


def checkReigon(r):
    global regions
    if regions[r] == "nA":
        return True
    print("Try Again")
    return False
    


def checkBoard(x):
    
    row1 = [regions[x] for x in rowcol if x // 10 == 1]
    row2 = [regions[x] for x in rowcol if x // 20 == 1]
    row3 = [regions[x] for x in rowcol if x // 30 == 1]
    column1 = [regions[x] for x in rowcol if x % 10 == ]
    for i in row1:
        print(i)
    for i in row2:
        print(i)
    for i in row3:
        print(i)
    
    if row1[1] and row1[2] and row1[3] == "x": #Checking the top row
        return "x"
    elif row1[1] and row1[2] and row1[3] == "o":
        return "o"
    elif row2[1] and row2[2] and row2[3] == "x": #Checking middle Row
        return "x"
    elif row2[1] and row2[2] and row2[3] == "o":
        return "o"
    elif row3[1] and row3[2] and row3[3] == "x": #Checking bottom row
        return "x"
    elif row3[1] and row3[2] and row3[3] == "o":
        return "o"
    

    








    
boardCreate()
penup()
goto(0,0)
onscreenclick(clickLocation)   
mainloop()






  
        

