import pygame





WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


class Player:
    def __init__(self):
        self.max_health = 100
        self.health = self.max_health


    def take_damage(self, amount):
        self.health = max(0, self.health - amount)


    def draw(self, screen, player_x, player_y):
        self.draw_health_bar(screen, player_x, player_y)


    def draw_health_bar(self, screen, player_x, player_y):

        bar_width = 100
        bar_height = 10
        bar_x = player_x + 10
        bar_y = player_y - 20



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
