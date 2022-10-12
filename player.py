from email.errors import HeaderParseError
import pygame


class Player:
    velocity = 20
    headPos = [60, 20]
    bodyCoordinates = [[60, 20], [40, 20], [20, 20]]
    direction = "down"
    newDirection = "down" 
    
    def __init__(self):
        pass
    
    def moveSnake(self):
        if (self.direction == "right"):
            del self.bodyCoordinates[-1]
            self.bodyCoordinates.insert(0, [self.headPos[0] + self.velocity, self.headPos[1]])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "left"):
            del self.bodyCoordinates[-1]
            self.bodyCoordinates.insert(0, [self.headPos[0] - self.velocity, self.headPos[1]])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "up"):
            del self.bodyCoordinates[-1]
            self.bodyCoordinates.insert(0, [self.headPos[0] , self.headPos[1] - self.velocity])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "down"):
            del self.bodyCoordinates[-1]
            self.bodyCoordinates.insert(0, [self.headPos[0] , self.headPos[1] + self.velocity])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]

    def drawSnake(self, surface):
        green = (0, 255, 0)
        for item in self.bodyCoordinates:
            pygame.draw.rect(surface, green, pygame.Rect(item[0],item[1], 20, 20)) #   20 width and height
        
    def increaseLength(self):
        if (self.direction == "right"):
            self.bodyCoordinates.insert(0, [self.headPos[0] + self.velocity, self.headPos[1]])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "left"):
            self.bodyCoordinates.insert(0, [self.headPos[0] - self.velocity, self.headPos[1]])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "up"):
            self.bodyCoordinates.insert(0, [self.headPos[0] , self.headPos[1] - self.velocity])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
            
        if (self.direction == "down"):
            self.bodyCoordinates.insert(0, [self.headPos[0] , self.headPos[1] + self.velocity])
            #   Reset Head Pos
            self.headPos = self.bodyCoordinates[0]
    
    def collidesFood(self, foodObj):
        if self.headPos == [foodObj.x, foodObj.y]:
            foodObj.changeFoodPos()
            self.increaseLength()