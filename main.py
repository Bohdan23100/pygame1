import pygame

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

bg = pygame.image.load("images/bg.png")
player = pygame.image.load("images/Idle_right/Idle (1).png")
# color1 = screen.fill
# color2 =( 88, 176, 157 )
size = (100, 100)

walk_right = [
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_right/Walk (10).png"), size)
]

walk_left = [
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/walk_left/Walk (10).png"), size)
]

Idle_left = [
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_left/Idle (10).png"), size)
]

Idle_right = [
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/Idle_right/Idle (10).png"), size)
]

run_right = [
    pygame.transform.scale(pygame.image.load("images/run_right/Run (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_right/Run (10).png"), size)
]

run_left = [
    pygame.transform.scale(pygame.image.load("images/run_left/Run (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/run_left/Run (10).png"), size)

]

jump_right = [
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_right/Jump (10).png"), size)
]

jump_left = [
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (1).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (2).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (3).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (4).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (5).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (6).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (7).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (8).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (9).png"), size),
    pygame.transform.scale(pygame.image.load("images/jump_left/Jump (10).png"), size)
]

size = (100, 100)


player = pygame.transform.scale(player, size)


player_anim_count = 0
bg_x = 0

player_x = 150
player_speed = 5
player_speed_spead = 8
while True:

    # color1(color2)

    screen.blit(bg, (bg_x, 0))






    type_user= pygame.key.get_pressed()

    if type_user[pygame.K_LEFT] or type_user[pygame.K_a]:
        if type_user[pygame.K_LSHIFT] or type_user[pygame.K_RSHIFT]:
            screen.blit(run_left[player_anim_count], (player_x, 515))
            walk_left1 = True
            walk_right1 = False
            player_x -= player_speed_spead
        else:
            screen.blit(walk_left[player_anim_count], (player_x, 515))
            walk_left1 = True
            walk_right1 = False
            player_x -= player_speed
    elif type_user[pygame.K_RIGHT] or type_user[pygame.K_d]:
        if type_user[pygame.K_LSHIFT] or type_user[pygame.K_RSHIFT]:
            screen.blit(run_right[player_anim_count], (player_x, 515))
            walk_left1 = False
            walk_right1 = True
            player_x += player_speed_spead
        else:
            screen.blit(walk_right[player_anim_count], (player_x, 515))
            walk_left1 = False
            walk_right1 = True
            player_x += player_speed
    else:
        if walk_left1 == True:
            screen.blit(Idle_left[player_anim_count], (player_x, 515))
        elif walk_right1 == True:
            screen.blit(Idle_right[player_anim_count], (player_x, 515))
        else:
            screen.blit(Idle_right[player_anim_count], (player_x, 515))




    player_anim_count += 1
    if player_anim_count == len(Idle_right):
        player_anim_count = 0





    # if not jump1:
    #     if type_user[pygame.K_SPACE]:
    #         jump1 = True
    #     elif type_user[pygame.K_SPACE]:








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_m:
        #         color2 = ( 70, 79, 184 )

    clock.tick(20)
    pygame.display.update()
