from re import T
from winsound import PlaySound
import pygame, sys
import time
#  Import window.py
import window, food, player, assets

from pygame.locals import *
(WIDTH, HEIGHT) = (800, 600)
TILE = 20
SCORE = 0

#   Frame per second(FPS) 
clock = pygame.time.Clock()
fps = 15

lastTime = time.time()

#   Set window
window.setWindow()

snake = player.Player()

food = food.Food()

running = True
isGameOver = False

playSound = True

def drawBoundary():
    boundaryColor = (25, 100, 255)
    pygame.draw.rect(window.getWindow(), boundaryColor, pygame.Rect(0,0, WIDTH- TILE, 20)) #   20 width and height
    pygame.draw.rect(window.getWindow(), boundaryColor, pygame.Rect(0, HEIGHT - TILE, WIDTH, 20)) #   20 width and height
    pygame.draw.rect(window.getWindow(), boundaryColor, pygame.Rect(0,0, 20, HEIGHT)) #   20 width and height
    pygame.draw.rect(window.getWindow(), boundaryColor, pygame.Rect(WIDTH- TILE,0, 20, HEIGHT)) #   20 width and height


while(running):
    if (isGameOver):
        if playSound:
            assets.gameOverSound()
            playSound = False
            
        window.getWindow().fill((0, 0, 0 ))
        assets.showText(window.getWindow(), "Game Over", 400, 250, 25)
        assets.showText(window.getWindow(), f"Score : {SCORE}", 400, 300, 25)
        assets.showText(window.getWindow(), f"'SPACE' to Play Again and Press 'Q' to QUIT ", 400, 350, 25)
        
    else:
        window.getWindow().fill((0, 0, 0 ))
        
        
        drawBoundary()
        assets.showText(window.getWindow(), f'Score : {SCORE}', 650, 10, 15)
        food.drawFood(window.getWindow())
        snake.drawSnake(window.getWindow())
        snake.moveSnake()
        SCORE = snake.collidesFood(SCORE, food)
        isGameOver = snake.isGameOver(TILE, WIDTH, HEIGHT)

    for event in pygame.event.get():
        if (event.type == QUIT):
            running = False
            
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

        if user_input[K_SPACE] and isGameOver == True:
            isGameOver = False
            snake.resetSnake()
            playSound = True
            SCORE = 0
            
        if user_input[K_q]:
            running = False

    window.updateWindow()
        
    #   Fps or refresh rate
    clock.tick(fps)
