import pygame, sys, random, requests, datetime
from random import *
from pygame.locals import *
from requests import *
from datetime import *

pygame.init()
font = pygame.font.SysFont(None, 24)
#Getting Currernt Time
timeRow1 = datetime.now().strftime('%X %p')
timeRow2 = datetime.now().strftime('%A, %B %d, %Y')
#Variables
WIDTH = 1000
HEIGHT = 600
r = 0
g = 0
b = 0
maximumValue = 255
fps = 240

#How much to add/subtract
radd = randint(1, 5) * 0.1
gadd = randint(1, 5) * 0.1
badd = randint(1, 5) * 0.1



DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gradient Test ")
clock = pygame.time.Clock()
pygame.font.init()

rFLip = False
gFlip = False
bFlip = False


def changeColor():
    global rFLip, gFlip, bFlip, r, g, b, radd, badd, gadd
    #Checking R Switch
    if rFLip == False:
        r += radd
    else:
        r -= radd
    
    #Checking G Switch
    if gFlip == False:
        g += gadd
    else:
        g -= gadd

    #Checking B Switch
    if bFlip == False:
        b += badd
    else:
        b -= badd

    
    
    
    ##Changing Switch Values
    #255 to 0
    if r >= maximumValue:
        r = maximumValue
        rFLip = True
    elif g >= maximumValue:
        g = maximumValue
        gFlip = True
    elif b >= maximumValue:
        b = maximumValue
        bFlip = True

    #0 to 255
    if r <= 0:
        r = 1
        rFLip = False
    elif g <= 0:
        g = 1
        gFlip = False
    elif b <= 0:
        b = 1
        bFlip = False
def getCurrentTime(a):
    global timeRow1, timeRow2
    timeRow1 = datetime.now().strftime('%X %p')
    timeRow2 = datetime.now().strftime('%A, %B %d, %Y')
    if a == 0:
        return timeRow1
    elif a == 1:
        return timeRow2
    else:
        print("Error: Time Not Specified")



GREEN = (0,255,0)
pygame.draw.circle(DISPLAYSURF,GREEN, (WIDTH // 2, HEIGHT // 2), 100 , 100)

while True: #Main Game Loop
    changeColor()
    try:
        DISPLAYSURF.fill((r,g,b), rect=None, special_flags=0)
        
    except TypeError:
        print("-----------------------ERROR: Moving On-----------------------#_------------------")
    #print("r = " + str(r) + "; g = " + str(g) + "; b = " + str(b))
    pygame.display.set_caption("Gradient Test: r = " + str(r) + "; g = " + str(g) + "; b = " + str(b))
    
    a = font.render(str(getCurrentTime(0)), True, (r / 5, g /5, b /5 ))
    bb = font.render(str(getCurrentTime(1)), True, (r / 5, g /5, b /5 ))
    DISPLAYSURF.blit(a, (WIDTH / 2, HEIGHT / 2))
    DISPLAYSURF.blit(bb, (WIDTH / 2, (HEIGHT / 2) + (HEIGHT / 8))

    
    
    for event in pygame.event.get():
        if event.type == QUIT or event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
    clock.tick(fps)
    pygame.display.update()


