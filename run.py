import pygame
import sys
import numpy as np
import time
import random

pygame.init()

screen = pygame.display.set_mode((1000,800))

black = pygame.Color(20,20,20)
grey = pygame.Color(200,200,200)
full_black = pygame.Color(0,0,0)
yellow = pygame.Color(171,179,54)

def count_neighbours(cells, x, y):
    count = 0
    for i in [x-10, x, x+10]:
        for j in [y-10, y, y+10]:
            if (i,j) in cells: count += 1
    
    if (x, y) in cells: count -= 1
    
    return count

# Remove cells outside of the screen
def filter_border(cells):
    dc = set()
    for x, y in cells:
        if x < 0 or x > 990:
            dc.add((x,y))
        if y < 0 or y > 790:
            dc.add((x,y))
    return dc

# draw cell on the screen and update the cell matrix
def draw_cell(screen, cells, pos, alive):
    actual_pos_x, actual_pos_y = (pos[1] // 10)*10, (pos[0] // 10)*10
    if alive: #if the cell is going to live it gets different color
        pygame.draw.rect(screen, full_black, (actual_pos_y, actual_pos_x, 10, 10))
        pygame.draw.rect(screen, yellow, (actual_pos_y + 1, actual_pos_x +1, 8, 8))
        return (actual_pos_x, actual_pos_y)

    else:
        pygame.draw.rect(screen, full_black, (actual_pos_y, actual_pos_x, 10, 10))
        pygame.draw.rect(screen, black, (actual_pos_y + 1, actual_pos_x +1, 8, 8))
        return (actual_pos_x, actual_pos_y)
# Main logic for the cellular automata
def update(screen, cells, stopped):
    if not stopped:
        screen.fill(black)
        for x, y in filter_border(cells):
            cells.remove((x,y))
        potencial_cells = set()
        for x, y in cells:
            for i in [x-10, x, x+10]:
                for j in [y-10, y, y+10]:
                    potencial_cells.add((i,j))

        for x, y in cells:
            potencial_cells.remove((x,y))
        dead_cells = set()
        new_cells = set()
        for x, y in cells:
            an = count_neighbours(cells, x, y)
            if an < 2:
                dead_cells.add(draw_cell(screen, cells, (x,y), False))
            elif an > 3:
                dead_cells.add(draw_cell(screen, cells, (x,y), False))
            else:
                new_cells.add(draw_cell(screen, cells, (x,y), True))

        for x, y in potencial_cells:
            an = count_neighbours(cells, x, y)
            if an == 3:
                new_cells.add(draw_cell(screen, cells, (x,y), True))

        for x, y in dead_cells:
            cells.remove((y,x))
        for x, y in new_cells:
            cells.add((y,x))

cells = set()
screen.fill(black)
stopped = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stopped = not stopped
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                draw_cell(screen, cells, pos, True)
                cells.add(((pos[0]//10)*10,(pos[1]//10)*10))
                print(cells)
            if event.button == 3:
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, full_black, ((pos[0]//10)*10, (pos[1]//10)*10, 10, 10))
                cells.remove(((pos[0]//10)*10,(pos[1]//10)*10))
                print(cells)
        pygame.display.update()

    update(screen, cells, stopped)

    pygame.display.update()
    time.sleep(0.1)
