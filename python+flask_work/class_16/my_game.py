import pygame

pygame.init()

pygame.display.set_mode((600, 600))

stop_game = False

while stop_game == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True
            pygame.display.update()

pygame.threads()
