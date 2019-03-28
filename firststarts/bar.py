import pygame

class Bar(pygame.sprite.Sprite):
    def __init__(self, unit, color, width, height):
        super().__init__()
        self.unit_value = unit
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [50,60,width,height])
        self.rect = self.image.get_rect()
