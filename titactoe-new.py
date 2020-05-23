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
        return None
    
    

def clickLocation(x,y):
    global regions
    global person
    
    goto(x,y)
    region = reigonFinder(x,y)
    checkBoardResult = checkBoard(region)
    if region != None:
        if checkBoardResult == "no" or checkBoardResult == "nA"  :  
            if  checkReigon(region) == True:
                if person == True:
                    drawX(squareCenter[region])
                    regions.update(region="X")
                else:
                    drawO(squareCenter[region])
                    regions.update(region="O")
                person = not person
        else: #Ending Sequence
            penup()
            goto(info)
            write(checkBoardResult + " has won the game")
            sety(ycor() - l)
            write("Click The Board To Exit")
            print(checkBoardResult + " has won the game \n Good Game! \n\n\n\n\nClick The Board To Exit")
            onscreenclick(gameOver)
            return     
    else:
        print("Try again!")

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
    column1 = [regions[x] for x in rowcol if x % 10 == 1]
    column2 = [regions[x] for x in rowcol if x % 10 == 2]
    column3 = [regions[x] for x in rowcol if x % 10 == 3]
    for i in row1:
        print(i)
    for i in row2:
        print(i)
    for i in row3:
        print(i)

    
    for i in [row1,row2,row3]:
        if i[0] == i[1] == i [2]:
            return i[1]
    for i in [column1,column2,column3]:
        if i[0] == i[1] == i [0]:
            return i[1]
    
    
    if row1[0] == row2[1] == row3[2] == "x":
        return "x"
    elif row1[0] == row2[1] == row3[2] == "o":
        return "o"
    elif row1[2] == row2[1] == row3[0] == "x":
        return "x"
    elif row1[2] == row2[1] == row3[0] == "o":
        return "o"
    else:
        return "no"

def gameOver(x,y): #Game Closer, gets set as the function that gets run in onscreenclick()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #"Clearing" The Screen
    exit(2010001110110000101101101011001010010000001000011011011000110111101110011011001010110010000100001) #Game Closed in Binary

boardCreate()
penup()
goto(0,0)
onscreenclick(clickLocation)   
mainloop()






  
        

