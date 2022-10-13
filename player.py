import pygame
import assets


class Player:
    velocity = 20
    headPos = [60, 20]
    bodyCoordinates = [[60, 20], [40, 20], [20, 20]]
    direction = "down"
    newDirection = "down" 
    
    def __init__(self):
        pass
    
    def resetSnake(self):
        self.velocity = 20
        self.headPos = [60, 20]
        self.bodyCoordinates = [[60, 20], [40, 20], [20, 20]]
        self.direction = "down"
        self.newDirection = "down" 
        
    def moveSnake(self):
        
        # Delete last element of list and insert to first position as per direction
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
        bodyColor = (2, 70, 22)
        headColor = (3, 4, 120)

        for item in self.bodyCoordinates:
            if (item == self.bodyCoordinates[0]):
                color = headColor
            else:
                color = bodyColor
            pygame.draw.rect(surface, color, pygame.Rect(item[0],item[1], 20, 20)) #   20 width and height
        
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
    
    def collidesFood(self,score, foodObj):
        
        #   if head and food have same co-ordinates
        if self.headPos == [foodObj.x, foodObj.y]:
            score += 5
            foodObj.changeFoodPos()
            self.increaseLength()
            assets.eatSound()
        return score
            
    def isGameOver(self, tile, width, height):
        
        #   Collision with body        
        for item in self.bodyCoordinates[1:]:
            if item == self.bodyCoordinates[0]:
                return True
                
                
        #   Out of bounds
        [headX, headY] = self.headPos
        if (headX < 20 or headX>(width - 2 * tile)):
            return True
            
        if (headY < 20 or headY>(height - 2 * tile)):
            return True
            
