import pygame
# run pygame page
pygame.init()

# the screen and the size of it
screen = pygame.display.set_mode([450, 450])

# the player in the size of the screen
player1 = pygame.image.load('red.png')
player2 = pygame.image.load('black.png')


# board color and rec
black = (0, 0, 0)
white = (255, 255, 255)


# draw rectngl 
def draw_rec(color, Ys, Xs,):
    Rsize = 80
    pygame.draw.rect(screen, color, [Ys, Xs, Rsize, Rsize])


def pylear1():
    screen.blit(player1,(8,5))
    screen.blit(player1, (175, 5))


def pylear2():
    screen.blit(player2,(8,260))


# all pise in the board
def all_board():
    draw_rec(black, 0, 0)
    draw_rec(white, 86, 0)
    draw_rec(black, 170, 0)
    draw_rec(white, 254, 0)

    draw_rec(white, 0, 86)
    draw_rec(black, 86, 86)
    draw_rec(white, 170, 86)
    draw_rec(black, 254, 86)

    draw_rec(black, 0, 170)
    draw_rec(white, 86, 170)
    draw_rec(black, 170, 170)
    draw_rec(white, 254, 170)

    draw_rec(white, 0, 254)
    draw_rec(black, 86, 254)
    draw_rec(white, 170, 254)
    draw_rec(black, 254, 254)


# the main loop for the game
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((126, 145, 131))
    all_board()
    pylear1()
    pylear2()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos(pylear2()):
            screen.blit(player2, (8, 10))


    pygame.display.update()
pygame.quit()
