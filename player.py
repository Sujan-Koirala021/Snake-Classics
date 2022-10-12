import pygame

from pygame.locals import *

class Snake:
    width = 20
    height = 20
    snake_body = [
        [100, 50],
        [80, 50],
        [60, 50]
    ]
    position = [100, 50] 
    direction = "right"
    movesTo = "right"
    
    def __init__(self, window):
        self.window = window
        pass
    

    def drawSnake(self):
        for item in self.snake_body:
            green = (0, 255, 0)
            pygame.draw.rect(self.window, green, (item[0], item[1], self.width, self.height))
            
            
    def checkBoundary(self, width, height):
        if (self.position[0] > width-self.position[0]):
            self.position[0] = 0
        
            if self.position[0]<0:
                self.position[0] = width - self.position[0]
        
            if self.position[1] <0:
                self.position[1] = height - self.position[0] 
            
            if self.position[1] > height - self.position[1]:
                self.position[1] = 0
            
    def hasCollided(self, foody):
        head = self.body_list[0]
        if (foody.x == head.x and foody.y == head.y):
            # self.SCORE += 1
            foody.changeFoodPos()
            return True

    def avoidUnnecessaryMotion(self):
        if (self.movesTo == "up" and self.direction!="down"):
            self.direction = "up"
            
        if (self.movesTo == "down" and self.direction!="up"):
            self.direction = "down"
            
        if (self.movesTo == "right" and self.direction!="left"):
            self.direction = "right"
            
        if (self.movesTo == "left" and self.direction!="right"):
            self.direction = "left"
        
        
    def moveSnake(self):
        self.avoidUnnecessaryMotion()
        
        if self.direction == "up":
            print("hi")
            print(self.position)
            self.position[1] -= 20 # means y pos decreased
            
        if self.direction == "down":
            self.position[1] += 20 
            
        if self.direction == "left":
            self.position[0] -= 20 

        if self.direction == "right":
            self.position[0] += 20 