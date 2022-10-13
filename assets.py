#   Sound and Text Assets

import pygame

def eatSound():
    sound = pygame.mixer.Sound('src/eatSound.wav')
    sound.play()
    
def gameOverSound():
    sound = pygame.mixer.Sound('src/gameOver.wav')
    sound.play()

def showText(win, your_text, posX, posY, text_size):
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', text_size)
    text = font.render(your_text, True, white)
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    win.blit(text, textRect)