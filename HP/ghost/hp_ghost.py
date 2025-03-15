import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        self.max_health = 50
        self.health = self.max_health

    def take_damage_ghost(self, amount):
        self.health = max(0, self.health - amount)

    def draw_ghost(self, screen, ghost_x, ghost_y):
        self.draw_health_bar(screen, ghost_x, ghost_y)

    def draw_health_bar(self, screen, ghost_x, ghost_y):

        bar_width = 100
        bar_height = 10
        bar_x = ghost_x - 20
        bar_y = ghost_y - 20

        health_percentage = self.health / self.max_health
        health_width = int(bar_width * health_percentage)

        if health_percentage > 0.6:
            color = GREEN
        elif health_percentage > 0.3:
            color = YELLOW
        else:
            color = RED

        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), border_radius=5)

        pygame.draw.rect(screen, color, (bar_x, bar_y, health_width, bar_height), border_radius=5)