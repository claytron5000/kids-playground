import pygame
from bar import Bar
from frame import Frame

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
DARKGREY = (125, 125, 125)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (255, 0, 0)

SCREENWIDTH=960
SCREENHEIGHT=960

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Small Bead Frame")

all_sprites_list = pygame.sprite.Group()

one_bar = Bar(1, DARKGREY, SCREENWIDTH, 10)
one_bar.rect.x = 0
one_bar.rect.y = 20

frame = Frame()

all_sprites_list.add(one_bar)
all_sprites_list.add(frame)

running = True
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    all_sprites_list.update()

    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
