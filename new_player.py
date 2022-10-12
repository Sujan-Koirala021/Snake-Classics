import pygame

from pygame.locals import *

class Player:
    SCORE = 0
    width = 20
    height = 20
    velocity = 1
    direction = "right"
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.win = win
    
    def drawRect(self):
        whiteColor = (255, 255, 255)
        pygame.draw.rect(self.win, whiteColor, (self.x, self.y, self.width, self.height))

    def drawPlayer(self):
        if (self.direction == "left"):
            self.x -= self.velocity;
        
        if (self.direction == "right"):
            self.x += self.velocity;
        
        if (self.direction == "up"):
            self.y -= self.velocity;    
        
        if (self.direction == "down"):
            self.y += self.velocity;
        
        self.drawRect()
    
    def moveLeft(self):
        if (self.direction != "right"):
            self.direction = "left"
        
    def moveRight(self):
        if (self.direction != "left"):
            self.direction = "right"

    def moveUp(self):
        if (self.direction != "down"):
            self.direction = "up"
        
    def moveDown(self):
        if (self.direction != "up"):
            self.direction = "down"

    def checkBoundary(self, width, height):
        if (self.x > width-self.width):
            self.x = 0
        
        if self.x<0:
            self.x = width - self.width
        
        if self.y <0:
            self.y = height - self.width 
            
        if self.y > height - self.height:
            self.y = 0
            
    def checkCollision(self, foody):
        distance = ((self.x - foody.x)**2 + (self.y - foody.y)**2)**(0.5)
        if (distance < 20):
            self.SCORE += 1
            foody.changeFoodPos()
            self.drawPlayer()


        
