import pygame
import sys
import numpy as numpy
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000,800))

black = pygame.Color(10,10,10)
grey = pygame.Color(200,200,200)

index = 0
screen.fill(black)
while True:
    left = (index % 10) * 100
    top = (index // 10) * 100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, grey, (left,top,100,100))
                index += 1
        pygame.display.update()

    pygame.display.update()
    time.sleep(0.1)
