import pygame
import keloger

pygame.init()
wind = pygame.display.set_mode((500, 500))
x = 0
y = 0

wiedh = 20
hieat = 10

pygame.draw.rect(wind,(200, 250, 250),(x, y, hieat, wiedh))
pygame.display.update()



