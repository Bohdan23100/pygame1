import pygame
import random
from CLASS.player.player import Player

class Heart(pygame.sprite.Sprite):
    # Клас для кожного серця
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/heart/heart_png.jpg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # Малюємо серце
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Додаємо здоров'я
    def hp(self, player):
        if player.health < 100:
            player.health = min(player.health + 10, 100)

