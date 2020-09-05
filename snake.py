import pygame.sprite , pygame, random, time
from pygame import *
from pygame.sprite import *


WIDTH = 647
HEIGHT = 647
pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
jumpInterval = 10
gameOver = True

x1_change = 0
y1_change = 0

x1 = WIDTH / 2
y1 = HEIGHT / 2

clock = pygame.time.Clock()


def loopback():
    global x1, x1_change, y1, y1_change
    if x1 >= WIDTH:
        x1 = 0
    elif x1 <= 0:
        x1 = WIDTH
    elif y1 >= HEIGHT:
        y1 = 0
    elif y1 <= 0:
        y1 = HEIGHT

while gameOver: #Game Loop




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = jumpInterval * -1
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = jumpInterval * 1
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = jumpInterval * -1
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = jumpInterval * 1
                x1_change = 0
    
    loopback()
    x1 += x1_change
    y1 += y1_change
    
    #Make Snake!
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (0, 255, 0), [x1, y1, 10, 10])
    
    #Food
    
    
    
    pygame.display.update()
    clock.tick(30)
