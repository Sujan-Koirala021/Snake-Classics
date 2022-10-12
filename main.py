import pygame, sys
import time
#  Import window.py
import window, events, food, player 

from pygame.locals import *
(WIDTH, HEIGHT) = (800, 600)

#   Frame per second(FPS) 
fps = pygame.time.Clock()

#   Set window
window.setWindow()
playerObj = player.Snake(window.getWindow())


food = food.Food()
while(True):
    window.getWindow().fill((0, 0, 0 ))
    food.drawFood(window.getWindow())
    
    
    events.quitEvent()
    events.keyPress(playerObj)
    
    playerObj.drawSnake()
    playerObj.moveSnake()
    print(playerObj.snake_body)
    playerObj.checkBoundary(WIDTH, HEIGHT)

    #   Increase length after eating food
    # if (playerObj.hasCollided(food)):
    #     headDir = playerObj.getHeadDirection()

    #     if headDir == "right":
    #         (x, y) = (playerObj.getHeadX()+20, playerObj.getHeadY())
        
    #     elif headDir == "left":
    #         (x, y) = (playerObj.getHeadX()-20, playerObj.getHeadY())
        
    #     elif headDir == "up":
    #         (x, y) = (playerObj.getHeadX(), playerObj.getHeadY() - 20)
            
    #     else:
            # (x, y) = (playerObj.getHeadX(), playerObj.getHeadY() + 20)

        
    window.updateWindow()
    
    #   Fps or refresh rate
    fps.tick(15)
