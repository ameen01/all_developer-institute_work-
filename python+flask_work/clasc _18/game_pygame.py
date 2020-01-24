import pygame

pygame.init()
scren = pygame.display.set_mode((800, 800))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
