import pygame, sys

from pygame.locals import *


def setWindow():
    global win
    pygame.init()

    win = pygame.display.set_mode((800 ,600))

def getWindow():
    return win
    
def updateWindow():
    pygame.display.update()