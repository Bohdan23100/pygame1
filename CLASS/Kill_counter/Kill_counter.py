import pygame

class KillCounter:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font
        self.kills = 0

    def add_kill(self):
        self.kills += 1

    def draw(self, screen):
        text_surface = self.font.render(f"Kills: {self.kills}", True, (255, 255, 255))
        screen.blit(text_surface, (self.x, self.y))