import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF= pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')




GREEN = (0,255,0)
pygame.draw.circle(DISPLAYSURF,GREEN, (0,0), 100 , 100)

while True: #Main Game Loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
        


