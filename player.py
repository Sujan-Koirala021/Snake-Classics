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
        red = (255, 0, 0)

        for item in self.bodyCoordinates:
            if (item == self.bodyCoordinates[0]):
                color = red
            else:
                color = green
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
    
    def collidesFood(self, foodObj):
        if self.headPos == [foodObj.x, foodObj.y]:
            foodObj.changeFoodPos()
            self.increaseLength()
            
    def gameOver(self, tile, width, height):
        for item in self.bodyCoordinates[1:]:
            if item == self.bodyCoordinates[0]:
                print("Game Over") 
                
        [headX, headY] = self.headPos
        if (headX < 20 or headX>(width - tile)):
            print("Game Over 2")
            
        if (headY < 20 or headY>(height - tile)):
            print("Game Over 3")