from turtle import *
from tkinter import *
from math import *
def boardCreate():
    goto(0,0)
    board.pendown()
    board.fd(75)
    board.bk(50)
    board.rt(90)
    board.fd(100)
    board.bk(50)
    board.lt(90)
    board.fd(50)
    board.bk(100)
    board.rt(90)
    board.fd(50)
    board.bk(150)
    board.fd(50)
    board.rt(90)
    board.fd(50)
    board.bk(100)
    board.rt(90)
    board.fd(50)
    board.bk(100)
    board.lt(90)
    board.fd(100)

def drawLabels():
    letters.clear()
    letters.seth(180)
    letters.goto(-75,-50)
    letters.penup()
    letters.bk(25)
    letters.rt(90)
    letters.forward(25)
    a2 = letters.pos()
    print(a2)
    letters.write(a2s)
    letters.forward(50)
    a1 = letters.pos()
    print(a1)
    letters.write(a1s)
    letters.rt(90)
    letters.forward(50)
    b1 = letters.pos()
    print(b1)
    letters.write(b1s)
    letters.forward(50)
    c1 = letters.pos()
    print(c1)
    letters.write(c1s)
    letters.rt(90)
    letters.forward(50)
    c2 = letters.pos()
    print(c2)
    letters.write(c2s)
    letters.forward(50)
    c3 = letters.pos()
    print(c3)
    letters.write(c3s)
    letters.rt(90)
    letters.forward(50)
    b3 = letters.pos()
    print(b3)
    letters.write(b3s)
    letters.forward(50)
    a3 = letters.pos()
    print(a3)
    letters.write(a3s)
    letters.bk(50)
    letters.rt(90)
    letters.forward(50)
    b2 = letters.pos()
    print(b2)
    letters.write(b2s)
    
ht()

speed(0)
penup()
board = clone()
win = "na"
p = 1

a1s = "a1"
a2s = "a2"
a3s = "a3"

b1s = "b1"
b2s = "b2"
b3s = "b3"

c1s = "c1"
c2s = "c2"
c3s = "c3"






goto(-75,-50)
lt(180)
goto(-75,-50)
letters = clone()
boardCreate()
drawLabels()
goto(-100.00,-225.00)

#Getting Og. Turtle in the right spot


#LAbels

#Bottom Text

penup()
bk(200)
lt(90)
fd(100)
rt(90)
print(pos())
text = pos()

while win == "na":

    if p == 1:
        clear()
        write("Player One's Turn", True, align="center")
        b = "x"
    else:
        clear()
        write("Player Two's Turn", True, align="center")
        b = "o"
    a = input()

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

    drawLabels()
    clear()


    # Win Conditions (X)
    
    #Rows
    if a1s == "x" and a2s == "x" and a3s == "x":
        win = "x"
        break
    if b1s == "x" and b2s == "x" and b3s == "x":
        win = "x"
        break
    if c1s == "x" and c2s == "x" and c3s == "x":
        win = "x"
        break

    #Coloums
    if a1s == "x" and b1s == "x" and c1s == "x":
        win = "x"
        break
    if a2s == "x" and b2s == "x" and c2s == "x":
        win = "x"
        break
    if a3s == "x" and b3s == "x" and c3s == "x":
        win = "x"
        break

    #Diaggonal 
    if a1s == "x" and b2s == "x" and c3s == "x":
        win = "x"
        break
    if a3s == "x" and b2s == "x" and c1s == "x":
        win = "x"
        break 



    # Win Conditions (O)
    #Rows
    if a1s == "o" and a2s == "o" and a3s == "o":
        win = "o"
        break
    if b1s == "o" and b2s == "o" and b3s == "o":
        win = "o"
        break
    if c1s == "o" and c2s == "o" and c3s == "o":
        win = "o"
        break

    #Coloums
    if a1s == "o" and b1s == "o" and c1s == "o":
        win = "o"
        break
    if a2s == "o" and b2s == "o" and c2s == "o":
        win = "o"
        break
    if a3s == "o" and b3s == "o" and c3s == "o":
        win = "o"
        break


    #Diaggonal 
    if a1s == "o" and b2s == "o" and c3s == "o":
        win = "o"
        break
    if a3s == "o" and b2s == "o" and c1s == "o":
        win = "o"
        break 



    drawLabels()
    clear()
    if p == 1:
        p = 0
    else:
        p = 1

clear()
if win == "x":
    write("Player One has won!", True, align="center")
else:
    write("Player Two has won!", True, align="center")


        
        



        
        

#Quack!
#Made by Child Duckling on Github (https://github.com/child-duckling)
