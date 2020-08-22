from turtle import *
from tkinter import *
from math import *

#Setup
l = 25
ht()
speed(0)
person = True #True - x ; False - o
regions = {10:"_", 11:"_", 12:"_", 20:"_", 21:"_", 22:"_", 30:"_", 31:"_", 32:"_"}
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
def convertModToReg(x):
    
    if x == 10:
        return 0
    elif x == 11:
        return 1
    elif x == 12:
        return 2
    elif x == 20:
        return 3
    elif x == 21:
        return 4
    elif x == 22:
        return 5
    elif x == 30:
        return 6
    elif x == 31:
        return 7
    elif x == 32:
        return 8
    else:
        return
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
            return 21
    else:
        print("Not on the board! \n ")
        return None
    
    

def clickLocation(x,y):
    global regions
    global person
    
    goto(x,y)
    region = reigonFinder(x,y)
    regRegion = convertModToReg(region)
    
    if region != None:

        if regions[region] == "_" :  
            if  checkReigon(region) == True:
                
                if person == True:
                    drawX(squareCenter[regRegion])
                    regions[region] = "x"
                else:
                    drawO(squareCenter[regRegion])
                    regions[region] = "o"
                person = not person
                if checkBoard(region) == "x" or checkBoard(region) == "o":#Ending Sequence
                    penup()
                    goto(info)
                    write(checkBoard(region) + " has won the game")
                    sety(ycor() - l)
                    write("Click the board to exit")
                    print(checkBoard(region) + " has won the game \n Good Game! \n\n\n\n\nClick The Board To Exit")
                    onscreenclick(gameOver)
                    return
            else:
                print("\nTry Again!")
        else: 
            print("\nTry Again!")
    else:
        print("\nTry again!")

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
    if regions[r] == "_":
        return True
    print("Try Again")
    return False
    


def checkBoard(x):
    
    row1 = [regions[x] for x in rowcol if x // 10 == 1]
    row2 = [regions[x] for x in rowcol if x > 19 and x < 23 ]
    row3 = [regions[x] for x in rowcol if x // 30 == 1]
    column1 = [regions[x] for x in rowcol if x % 10 == 0]
    column2 = [regions[x] for x in rowcol if x % 10 == 1]
    column3 = [regions[x] for x in rowcol if x % 10 == 2]
    print(len(row2))
    print("\nChecking Board....")
    print(row1)
    print(row2)
    print(row3)

    
    for i in [row1,row2,row3]:
        if i[0] == i[1] == i[2]:
            return i[1]
    for i in [column1,column2,column3]:
        if i[0] == i[1] == i[2]:
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
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #"Clearing" The Output
    exit(1010001110110000101101101011001010010000001000011011011000110111101110011011001010110010000100001) #Game Closed in Bi_ry

boardCreate()
penup()
goto(0,0)
onscreenclick(clickLocation)   
mainloop()






  
        

