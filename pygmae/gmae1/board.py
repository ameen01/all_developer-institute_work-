import pygame

pygame.init()

screen = pygame.display.set_mode([450, 450])


player1 = pygame.image.load('red.png')

player2 = pygame.image.load('black.png')

screen.blit(player1,(8,5))
screen.blit(player2, (175, 5))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((14, 25, 66))
    screen.blit(player1, (8, 5))
    screen.blit(player2, (175, 5))
    for pygame.MOUSEBUTTONDOWN:
        screen.blit(player1, (86, 5))




    pygame.display.update()
pygame.quit()