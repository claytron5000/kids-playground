import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


pygame.init()
pygame.display.set_caption("Montessori Classroom")

screen_width = 480
screen_height = 480
screen = pygame.display.set_mode([screen_width, screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 40, 40)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)

player = Block(RED, 40, 40)
all_sprites_list.add(player)
movement = 20

done = False
clock = pygame.time.Clock()
score = 0
clicked = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 273:
                player.rect.y = player.rect.y - movement
            elif event.key == 274:
                player.rect.y = player.rect.y + movement
            elif event.key == 276:
                player.rect.x = player.rect.x - movement
            elif event.key == 275:
                player.rect.x = player.rect.x + movement
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.rect.x = pygame.mouse.get_pos()[0]
            player.rect.y = pygame.mouse.get_pos()[1]
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        elif event.type == pygame.MOUSEMOTION and clicked:
            player.rect.x = pygame.mouse.get_pos()[0]
            player.rect.y = pygame.mouse.get_pos()[1]

    screen.fill(WHITE)

    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in block_hit_list:
        score += 1
        print(score)
    if score == 50:
        print("YOU WIN!!!!")
        done = True
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
