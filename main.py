import pygame, sys
import time
#  Import window.py
import window, food, player 

from pygame.locals import *
(WIDTH, HEIGHT) = (800, 600)

#   Frame per second(FPS) 
clock = pygame.time.Clock()
fps = 15

lastTime = time.time()

#   Set window
window.setWindow()

snake = player.Player()

food = food.Food()
while(True):
    
    window.getWindow().fill((0, 0, 0 ))
    food.drawFood(window.getWindow())
    snake.drawSnake(window.getWindow())
    snake.moveSnake()
    snake.collidesFood(food)
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()
            
        user_input = pygame.key.get_pressed()
    
        #   Check for keypress
        if user_input[K_RIGHT]:
            snake.newDirection = "right"
            if snake.direction != "left":
                snake.direction = snake.newDirection
                        
        if user_input[K_LEFT]:
            snake.newDirection = "left"
            if snake.direction != "right":
                snake.direction = snake.newDirection

        if user_input[K_UP]:
            snake.newDirection = "up"
            if snake.direction != "down":
                snake.direction = snake.newDirection

        if user_input[K_DOWN]:
            snake.newDirection = "down"
            if snake.direction != "up":
                snake.direction = snake.newDirection

    window.updateWindow()
        
    #   Fps or refresh rate
    clock.tick(fps)
