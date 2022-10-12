import pygame
from pygame.locals import *


import random


class Food:
    color = (255, 0 , 255)
    (width, height) = (20, 20) 
    def __init__(self):
        (self.x , self.y) = (random.randrange(20, 800 - 40, 20), random.randrange(20,  600 - 40, 20))

        
    def changeFoodPos(self):
        (self.x , self.y) = (random.randrange(20, 800 - 40, 20), random.randrange(20,  600 - 40, 20))
        
    def drawFood(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
    
    