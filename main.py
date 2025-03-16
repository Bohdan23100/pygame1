import pygame
from Moves.walk_right import walk_right
from Moves.walk_left import walk_left
from Moves.jump_right import jump_right
from Moves.jump_left import jump_left
from Moves.run_right import run_right
from Moves.run_left import run_left
from Moves.Idle_left import Idle_left
from Moves.Idle_right import Idle_right
from CLASS.player.player import Player
from Moves.ghost_right import ghost_right
from Moves.ghost_left import ghost_left
from CLASS.ghost.ghost import Ghost
from Moves.attack_right import attack_right
from Moves.attack_left import attack_left
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1280,748))     #flags=pygame.NOFRAME
pygame.display.set_caption("Pygame Bohdan Game")
icon = pygame.image.load("images/game-development.png")
pygame.display.set_icon(icon)

walk_right1 = False
walk_left1 = False
jump_right1 = False
jump_left1 = False
ghost_right1 = False
ghost_left1 = False
attack = False
jump1 = False
size = (100, 100)
size_ghost = (70, 70)
bg = pygame.image.load("images/bg.png")




# color1 = screen.fill
# color2 =( 88, 176, 157 )






player_anim_count = 0
bg_x = 0

player_x = 150
player_y = 515
start_y = player_y
jump_count = 8
player_speed = 5
player_speed_spead = 8



ghost_y = 530
ghost_speed = 4

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


ghosts = [Ghost(ghost_right, ghost_left, ghost_speed) for _ in range(5)]
ghosts.append(Ghost(ghost_right, ghost_left, ghost_speed))
player_hp = Player()
while True:


    # 🎨 Відображення фону
    screen.blit(bg, (bg_x, 0))



    # 🏃‍♂️ Отримання хитбоксу гравця
    player_rect = Idle_right[0].get_rect(topleft=(player_x, player_y))

    # 👽 Перевірка зіткнення гравця з привидом (отримання урону)
    for ghost in ghosts:
        ghost_rect = ghost.image_right.get_rect(topleft=(ghost.x, ghost.y))
        if player_rect.colliderect(ghost_rect):
            player_hp.take_damage(0.5)
            print(f"Здоров'я гравця: {player_hp.health}")

    # 🔄 Оновлення всіх ворогів
    for ghost in ghosts:
        ghost.move(player_x)
        ghost.draw(screen)

    # ❤️ Відображення CLASS гравця
    player_hp.draw(screen, player_x, player_y)







    # 💀 Перевірка на кінець гри, якщо CLASS = 0
    if player_hp.health <= 0:
        print("Game Over")
        break

    # 👻 Видаляємо мертвих привидів і створюємо нових
    ghosts = [ghost for ghost in ghosts if ghost.health > 0]
    while len(ghosts) < 5:
        ghosts.append(Ghost(ghost_right, ghost_left, ghost_speed))

    # ⌨️ Отримання натиснутих клавіш
    type_user = pygame.key.get_pressed()

    # ⚔️ Атака гравця по натисненню "F"
    attack = False
    if type_user[pygame.K_f]:
        attack = True
        if walk_right1 and not walk_left1:
            screen.blit(attack_right[player_anim_count], (player_x, player_y))
        elif walk_left1 and not walk_right1:
            screen.blit(attack_left[player_anim_count], (player_x, player_y))

        # 🔥 Перевірка дистанції атаки для кожного привида
        for ghost in ghosts:
            ghost_rect = ghost.image_right.get_rect(topleft=(ghost.x, ghost.y))
            distance = abs(player_rect.x - ghost_rect.x)

            if distance < 30:
                ghost.take_damage(1)
                print(f"Здоров'я привида: {ghost.health}")


    # ⬅️➡️ Рух гравця вліво/вправо
    if attack == False:
        if (type_user[pygame.K_LEFT] or type_user[pygame.K_a]) and player_x > 50:
            if type_user[pygame.K_LSHIFT] or type_user[pygame.K_RSHIFT]:
                if not jump1:
                    screen.blit(run_left[player_anim_count], (player_x, player_y))
                    walk_left1 = True
                    walk_right1 = False
                player_x -= player_speed_spead
            else:
                if not jump1:
                    screen.blit(walk_left[player_anim_count], (player_x, player_y))
                    walk_left1 = True
                    walk_right1 = False
                player_x -= player_speed

        elif (type_user[pygame.K_RIGHT] or type_user[pygame.K_d]) and player_x < 1100:
            if type_user[pygame.K_LSHIFT] or type_user[pygame.K_RSHIFT]:
                if not jump1:
                    screen.blit(run_right[player_anim_count], (player_x, player_y))
                    walk_left1 = False
                    walk_right1 = True
                player_x += player_speed_spead
            else:
                if not jump1:
                    screen.blit(walk_right[player_anim_count], (player_x, player_y))
                    walk_left1 = False
                    walk_right1 = True
                player_x += player_speed

        else:
            if walk_left1:
                if not jump1:
                    screen.blit(Idle_left[player_anim_count], (player_x, player_y))
            elif walk_right1:
                if not jump1:
                    screen.blit(Idle_right[player_anim_count], (player_x, player_y))
            else:
                screen.blit(Idle_right[player_anim_count], (player_x, player_y))



    # 🔄 Оновлення анімації
    player_anim_count += 1
    if player_anim_count == len(Idle_right):
        player_anim_count = 0



    # 🦘 Стрибок гравця
    if not jump1:
        if attack == False:
            if type_user[pygame.K_SPACE] and 50 < player_x < 1100:
                jump1 = True
    else:
        if jump_count >= -8:
            move_y = (jump_count ** 2) / 2 * (-1 if jump_count > 0 else 1)
            player_y += move_y

            if type_user[pygame.K_LEFT] or type_user[pygame.K_a]:
                player_x -= player_speed * 0.5
                screen.blit(jump_left[player_anim_count], (player_x, player_y))
            elif type_user[pygame.K_RIGHT] or type_user[pygame.K_d]:
                player_x += player_speed * 0.5
                screen.blit(jump_right[player_anim_count], (player_x, player_y))
            else:
                if walk_left1:
                    screen.blit(jump_left[player_anim_count], (player_x, player_y))
                elif walk_right1:
                    screen.blit(jump_right[player_anim_count], (player_x, player_y))
                else:
                    screen.blit(jump_right[player_anim_count], (player_x, player_y))

            jump_count -= 1
        else:
            jump1 = False
            jump_count = 8
            player_y = start_y



    # 🖱️ Перевірка подій (вихід з гри)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    # ⏳ Оновлення гри
    clock.tick(28)
    pygame.display.update()
