import pygame
from Moves.walk_right import walk_right
from Moves.walk_left import walk_left
from Moves.jump_right import jump_right
from Moves.jump_left import jump_left
from Moves.run_right import run_right
from Moves.run_left import run_left
from Moves.Idle_left import Idle_left
from Moves.Idle_right import Idle_right
from HP.player.hp_player import Player

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
jump1 = False
size = (100, 100)
bg = pygame.image.load("images/bg.png")
player = pygame.image.load("images/Idle_right/Idle (1).png")
ghost_right = pygame.transform.scale(pygame.image.load("images/ghost/ghost_right.png"), size)
ghost_left = pygame.transform.scale(pygame.image.load("images/ghost/ghost_right.png"), size)

# color1 = screen.fill
# color2 =( 88, 176, 157 )



player = pygame.transform.scale(player, size)


player_anim_count = 0
bg_x = 0

player_x = 150
player_y = 515
start_y = player_y
jump_count = 7
player_speed = 5
player_speed_spead = 8

ghost_left_x = 500
ghost_right_x = 1280
ghost_y = 500


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

player_hp = Player()

while True:

    # color1(color2)



    # player_hp.take_damage(80)

    screen.blit(bg, (bg_x, 0))
    screen.blit(ghost_right, (ghost_right_x, ghost_y))
    screen.blit(ghost_left, (ghost_left_x, ghost_y))



    player_rect = Idle_right[0].get_rect(topleft=(player_x, player_y))

    ghost_left_rect = ghost_left.get_rect(topleft=(ghost_left_x,ghost_y))
    ghost_right_rect = ghost_right.get_rect(topleft=(ghost_right_x,ghost_y))



    player_hp.draw(screen, player_x, player_y)




    if player_rect.colliderect(ghost_left_rect) or player_rect.colliderect(ghost_right_rect):
        player_hp.take_damage(0.5)
        print(f"Здоров'я гравця: {player_hp.health}")

    if player_hp.health == 0:
        print("Game Over")
        break




    type_user= pygame.key.get_pressed()

    if type_user[pygame.K_LEFT] or type_user[pygame.K_a] and player_x > 50:
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
    elif type_user[pygame.K_RIGHT] or type_user[pygame.K_d] and player_x < 1100:
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

    player_anim_count += 1
    if player_anim_count == len(Idle_right):
        player_anim_count = 0

    if not jump1:
        if type_user[pygame.K_SPACE] and 50 < player_x < 1100:
            jump1 = True
    else:
        if jump_count >= -7:
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
            jump_count = 7
            player_y = start_y



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_m:
        #         color2 = ( 70, 79, 184 )

    clock.tick(28)
    pygame.display.update()
