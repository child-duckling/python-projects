import pygame, sys, random, requests
from random import *
from pygame.locals import *
from requests import *
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

#Getting Currernt Time
time = requests.get('https://worldtimeapi.org/api/timezone/America/Anchorage')

#Variables
WIDTH = 400
HEIGHT = 400
r = 0
g = 0
b = 0

#How much to add/subtract
radd = 0.1 + randint(1, 5) * 0.01
gadd = 0.1 + randint(1, 5) * 0.01
badd = 0.1 + randint(1, 5) * 0.01



DISPLAYSURF= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gradient Test ")
clock = pygame.time.Clock()
fps = 240
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
    if r >= 255:
        r = 255
        rFLip = True
    elif g >= 255:
        g = 255
        gFlip = True
    elif b >= 255:
        b = 255
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




GREEN = (0,255,0)
pygame.draw.circle(DISPLAYSURF,GREEN, (WIDTH // 2, HEIGHT // 2), 100 , 100)

while True: #Main Game Loop
    changeColor()
    try:
        DISPLAYSURF.fill((r,g,b), rect=None, special_flags=0)
    except TypeError:
        print("ERROR: Moving On")
    print("r = " + str(r) + "; g = " + str(g) + "; b = " + str(b))
    
    

    
    
    for event in pygame.event.get():
        if event.type == QUIT or event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
    clock.tick(fps)
    pygame.display.update()


