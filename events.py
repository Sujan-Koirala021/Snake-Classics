import pygame, sys
from pygame.locals import *

def quitEvent():
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()

def keyPress(playerObj):    
    user_input = pygame.key.get_pressed()
    
    #   Check for keypress
    if user_input[K_RIGHT]:
        playerObj.movesTo = "right"
                    
    if user_input[K_LEFT]:
        playerObj.movesTo = "left"
        

    if user_input[K_UP]:
        playerObj.movesTo = "up"
            
    if user_input[K_DOWN]:
        playerObj.movesTo = "down"

        