import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacleMovement(obList):
    if obList:
        for obstacleRect in obList:
            # moving obstacle to left
            obstacleRect.x -= 5
            # to draw or snail
            if obstacleRect.bottom == 300:
                screen.blit(snail_surface, obstacleRect)
            # to draw for fly
            else:
                screen.blit(fly_surf, obstacleRect)
        # checking that if snail or fly goes out off screen so we remove them
        obList = [obstacle for obstacle in obList if obstacle.x > -100]
        # print(len(obList))
        return obList
    else:
        return []

def collisions(player, obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
game_active = False
clock = pygame.time.Clock()

player_surf = pygame.image.load("Resources/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

player_gravity = 0

sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()

test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)

scoreEndSurf = test_font.render("Keshav", False, (111, 195, 169))
scoreEmdRect = scoreEndSurf.get_rect(midbottom=(400, 100))
infoEndSurf = test_font.render("Press space to run", False, (111, 195, 169))
infoEmdRect = infoEndSurf.get_rect(midbottom=(400, 350))

# Obstacle
snail_surface = pygame.image.load("Resources/graphics/snail/snail1.png").convert_alpha()
# snail_rect = snail_surface.get_rect(midbottom=(680, 300))
fly_surf = pygame.image.load("Resources/graphics/fly/Fly1.png").convert_alpha()
obstacle_rect_list = []

start_time = 0

player_stand = pygame.image.load("Resources/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
score = 0
# Timer
# setting timer to spawn objet
obstacle_timer = pygame.USEREVENT+1
# help to set time
# arg1 = event, ars2 = milisec
pygame.time.set_timer(obstacle_timer, 900)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                if player_rect.bottom == 300:
                    player_gravity = -20
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20
        elif not game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    # snail_rect.left = 600
        if event.type == obstacle_timer and game_active:
            # to make enemy snail
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
            # to make enemy fly
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        # snail_rect.left -= 4
        # if snail_rect.left <= -100:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        # player_rect.y = 0
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacleMovement(obstacle_rect_list)

        # collisions
        game_active = collisions(player_rect, obstacle_rect_list)
    elif not game_active:
        start_time = int(pygame.time.get_ticks() / 1000)
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        # displaying score on 2nd state
        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(scoreEndSurf, scoreEmdRect)
        if score == 0:
            start_time = int(pygame.time.get_ticks() / 1000)
            screen.blit(infoEndSurf, infoEmdRect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
