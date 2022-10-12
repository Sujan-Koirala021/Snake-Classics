import pygame, sys
import time
#  Import window.py
import window, food, player 

from pygame.locals import *
(WIDTH, HEIGHT) = (800, 600)

#   Frame per second(FPS) 
fps = pygame.time.Clock()

#   Set window
window.setWindow()

food = food.Food()
while(True):
    window.getWindow().fill((0, 0, 0 ))
    food.drawFood(window.getWindow())

    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()
            
        user_input = pygame.key.get_pressed()
    
        #   Check for keypress
        if user_input[K_RIGHT]:
            pass
            # playerObj.movesTo = "right"
                        
        if user_input[K_LEFT]:
            pass
            # playerObj.movesTo = "left"
            

        if user_input[K_UP]:
            pass
            # playerObj.movesTo = "up"
                
        if user_input[K_DOWN]:
            pass
            # playerObj.movesTo = "down"
        
    window.updateWindow()
        
    #   Fps or refresh rate
    fps.tick(15)
