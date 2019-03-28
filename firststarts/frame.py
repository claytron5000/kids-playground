import pygame

class Frame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([620, 440])
        pygame.draw.rect(self.image, (120,30,60), [10,20, 420, 640], 5)
        self.rect = self.image.get_rect()
