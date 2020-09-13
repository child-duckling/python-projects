import pygame
import time
import random

pygame.init()
 




##These are the Custom Game Parameters


WIDTH = 500
HEIGHT = 500

#Ideal box size to speed is 1 to 3 
boxSize = 10
speed = 30 







if (WIDTH == 500 and HEIGHT == 500 and boxSize == 10 and speed == 30):
    print("Running Snake with default parameters")
else:
    print("Running Snake with custom parameters: \n-Height: " + str(HEIGHT) + 
    "\n-Width: " + str(WIDTH) +
    "\n-Box Size: " + str(boxSize) +
    "\n-Speed: " + str(speed))


gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
x1 = WIDTH / 2
y1 = HEIGHT / 2 
clock = pygame.time.Clock()
def our_snake(boxSize, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, (0,255,0), [x[0], x[1], boxSize, boxSize])

def loopback():
    global WIDTH, HEIGHT, x1, y1
    if x1 >= WIDTH:
        x1 = 0
    elif x1 < 0:
        x1 = WIDTH 
    elif y1 >= HEIGHT:
        y1 = 0 
    elif y1 < 0:
        y1 = HEIGHT
 

 
 
def gameLoop():
    global x1, y1, speed
    game_over = False
    game_close = False
 
    
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, WIDTH - boxSize) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - boxSize) / 10.0) * 10.0
 
    while not game_over:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -boxSize
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = boxSize
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -boxSize
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = boxSize
                    x1_change = 0
                elif event.key == pygame.K_k:
                    foodx = round(random.randrange(0, WIDTH - boxSize) / 10.0) * 10.0
                    foody = round(random.randrange(0, HEIGHT - boxSize) / 10.0) * 10.0
 
        loopback()
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill((0,0,0))
        pygame.draw.rect(gameDisplay, (255,0,0), [foodx, foody, boxSize, boxSize])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(boxSize, snake_List)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - boxSize) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - boxSize) / 10.0) * 10.0
            Length_of_snake += 1
            speed = speed - ((speed / speed) - (speed * 0.01))
        
        
 
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()