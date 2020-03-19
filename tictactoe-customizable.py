from turtle import *
from tkinter import *
from math import *
l = 50





def lineto(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)



def boardCreate():
    lineto(-0.5 * l, 1.5 * l, -0.5, -1.5 * l)
    lineto(0.5 * l, 1.5 * l, 0.5 * l, -1.5 * l)
    lineto(1.5 * l, 0.5 * l, -1.5 * l, 0.5 * l)
    lineto(1.5 * l, 0.5 * l, 1.5 * l, 0.5 * l)


    #Borders

    board.rt(90)
    board.fd(l * 2)
    board.rt(90)
    board.fd(l * 3)
    board.rt(90)
    board.fd(l * 3)
    board.rt(90)
    board.fd(l * 3)
    board.rt(90)
    board.fd(l * 3)

def drawLabels():
    letters.clear()
    letters.goto(letterStart)
    letters.penup()
    letters.bk(l - l)
    letters.rt(90)
    letters.forward(l - l)
    a2 = letters.pos()
    letters.write(a2s)
    letters.forward(l)
    a1 = letters.pos()
    letters.write(a1s)
    letters.rt(90)
    letters.forward(l)
    b1 = letters.pos()
    letters.write(b1s)
    letters.forward(l)
    c1 = letters.pos()
    letters.write(c1s)
    letters.rt(90)
    letters.forward(l)
    c2 = letters.pos()
    letters.write(c2s)
    letters.forward(l)
    c3 = letters.pos()
    letters.write(c3s)
    letters.rt(90)
    letters.forward(l)
    b3 = letters.pos()
    letters.write(b3s)
    letters.forward(l)
    a3 = letters.pos()
    letters.write(a3s)
    letters.bk(l)
    letters.rt(90)
    letters.forward(l)
    b2 = letters.pos()
    letters.write(b2s)


#Variables Setup
#ht()
speed(54)
penup()
board = clone()
win = "na"
p = 1
if l > 375:
    print("Screen Size too big! \n Aborting!")
    l = 50
##Squares
a1s = "a1"
a2s = "a2"
a3s = "a3"

b1s = "b1"
b2s = "b2"
b3s = "b3"

c1s = "c1"
c2s = "c2"
c3s = "c3"

#Setting up Turtles
##Setting up Screen
title("TicTacToe")
setup (width=l * 5, height= l * 5 + 100, startx=0, starty=0)
##Turtle Creater
goto((l + 15) * -1,l * -1)
lt(180)
goto((l + 15) * -1,l * -1)
letterStart = pos()
letters = clone()
boardCreate()
drawLabels()
goto(-100.00,-225.00)
delay(500)

#Bottom Text (Usualy doesn't showup, but its ther just in case)
penup()
bk(200)
lt(90)
fd(100)
rt(90)
text = pos()


#Gameplay
while win == "na":
    #Player Turn Detecter
    if p == 1:
        goto(text)
        clear()
        b = "x"
        a = textinput("Player One", "What Square?")
    else:
        clear()
        goto(text)
        a = textinput("Player Two", "What Square?")
        b = "o"

    #Square Changer
    if a == "a1":
        a1s = b
    elif a == "a2":
        a2s = b
    elif a == "a3":
        a3s = b
    elif a == "b1":
        b1s = b
    elif a == "b2":
        b2s = b
    elif a == "b3":
        b3s = b
    elif a == "c1":
        c1s = b
    elif a == "c2":
        c2s = b
    elif a == "c3":
        c3s = b
    else:
        continue #Restarts While Loop


    #Twice for compatability with larger numbers
    drawLabels()
    drawLabels()

    # Win Conditions (X)

    ##Rows
    if a1s == "x" and a2s == "x" and a3s == "x":
        win = "x"
        break
    if b1s == "x" and b2s == "x" and b3s == "x":
        win = "x"
        break
    if c1s == "x" and c2s == "x" and c3s == "x":
        win = "x"
        break

    ##Coloums
    if a1s == "x" and b1s == "x" and c1s == "x":
        win = "x"
        break
    if a2s == "x" and b2s == "x" and c2s == "x":
        win = "x"
        break
    if a3s == "x" and b3s == "x" and c3s == "x":
        win = "x"
        break

    ##Diaggonal
    if a1s == "x" and b2s == "x" and c3s == "x":
        win = "x"
        break
    if a3s == "x" and b2s == "x" and c1s == "x":
        win = "x"
        break



    # Win Conditions (O)
    ##Rows
    if a1s == "o" and a2s == "o" and a3s == "o":
        win = "o"
        break
    if b1s == "o" and b2s == "o" and b3s == "o":
        win = "o"
        break
    if c1s == "o" and c2s == "o" and c3s == "o":
        win = "o"
        break

    ##Coloums
    if a1s == "o" and b1s == "o" and c1s == "o":
        win = "o"
        break
    if a2s == "o" and b2s == "o" and c2s == "o":
        win = "o"
        break
    if a3s == "o" and b3s == "o" and c3s == "o":
        win = "o"
        break


    ##Diaggonal
    if a1s == "o" and b2s == "o" and c3s == "o":
        win = "o"
        break
    if a3s == "o" and b2s == "o" and c1s == "o":
        win = "o"
        break

    #Twice for compatability with larger numbers
    drawLabels()
    drawLabels()


    #Player Changer
    if p == 1:
        p = 0
    else:
        p = 1

clear()

#Twice to visually see who won
drawLabels()
drawLabels()

#Player win detecter
if win == "x":
    textinput("Player One","Player One has won!")
else:
    textinput("Player Two","Player Two has won!")

#Closing Window
bye()
