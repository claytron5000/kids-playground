import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (20, 235, 20)
BLUE = (0, 0, 255)
RED   = (255,   0,   0)


class Bead(pygame.sprite.Sprite):
    def __init__(self, color, value):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(color)
        self.unit_value = value
        self.rect = self.image.get_rect()

pygame.init()
pygame.display.set_caption("Montessori Classroom")

screen_width = 960
screen_height = 960
screen = pygame.display.set_mode([screen_width, screen_height])
bead_list = pygame.sprite.Group()


bead = Bead(GREEN, 1)
bead.rect.x = random.randrange(screen_width)
bead.rect.y = 80
bead_list.add(bead)

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    bead_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
