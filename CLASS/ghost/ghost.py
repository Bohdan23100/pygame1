import pygame
import random
from CLASS.Kill_counter.Kill_counter import KillCounter

# 🎨 Кольори для шкали здоров'я
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

class Ghost:
    def __init__(self, image_right, image_left, speed):
        # 👻 Випадкова початкова позиція (зліва або справа)
        if random.choice([True, False]):
            self.x = -50
        else:
            self.x = 1250

        self.y = 530

        # 🖼️ Спрайти привида
        self.image_right = image_right
        self.image_left = image_left

        # 🏃‍♂️ Швидкість руху
        self.speed = speed

        # ❤️ Здоров'я привида
        self.health = random.randint(5,10)
        self.max_health = self.health

        # 🔄 Напрямок руху
        self.direction = "left" if self.x > 600 else "right"

    # 🏃‍♂️ Переміщення привида
    def move(self, player_x):
        if abs(self.x - player_x) > 2:
            if self.x < player_x:
                self.x += self.speed
                self.direction = "right"
            else:
                self.x -= self.speed
                self.direction = "left"

    # 👻 Відображення привида та його HP
    def draw(self, screen):
        # Малюємо самого привида
        if self.direction == "right":
            screen.blit(self.image_right, (self.x, self.y))
        else:
            screen.blit(self.image_left, (self.x, self.y))

        # ⚕️ Малюємо HP бар
        bar_width = 50
        bar_height = 5
        bar_x = self.x + 10
        bar_y = self.y - 10

        health_percentage = self.health / self.max_health
        health_width = int(bar_width * health_percentage)

        if health_percentage > 0.6:
            color = GREEN
        elif health_percentage > 0.3:
            color = YELLOW
        else:
            color = RED

        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), border_radius=3)
        pygame.draw.rect(screen, color, (bar_x, bar_y, health_width, bar_height), border_radius=3)

    # ❤️ Відображення шкали здоров'я привида
    def draw_health_bar(self, screen):
        bar_width = 40
        bar_height = 5
        bar_x = self.x + 20
        bar_y = self.y - 10

        health_percentage = self.health / self.max_health
        health_width = int(bar_width * health_percentage)

        # 🎨 Вибір кольору залежно від рівня HP
        if health_percentage > 0.6:
            color = GREEN
        elif health_percentage > 0.3:
            color = YELLOW
        else:
            color = RED

        # ⚫ Малюємо чорний фон шкали HP
        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, bar_width, bar_height), border_radius=3)

        # 🔴 Малюємо саму шкалу HP
        pygame.draw.rect(screen, color, (bar_x, bar_y, health_width, bar_height), border_radius=3)

    # 💀 Отримання урону
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

