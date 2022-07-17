import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
clock = pygame.time.Clock()
sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()
test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)
# score_surf = test_font.render("Score", False, 'Black')
score_surf = test_font.render("Score", False, (64, 64, 64))
score_rect = score_surf.get_rect(midbottom=(400, 50))
snail_surface = pygame.image.load("Resources/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(680, 300))
player_surf = pygame.image.load("Resources/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect, width=10)
    pygame.draw.rect(screen, '#c0e8ec', score_rect)

    screen.blit(score_surf, score_rect)
    snail_rect.left -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    # Player
    # player_rect.y = 0
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)