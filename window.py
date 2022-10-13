import pygame, sys

from pygame.locals import *

# Initialize window
def setWindow():
    global win
    pygame.init()

    win = pygame.display.set_mode((800 ,600))
    pygame.display.set_caption("Snake Classics")

# Return window
def getWindow():
    return win
    
# Update window
def updateWindow():
    pygame.display.update()