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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # print true when any key is pressed
        if event.type == pygame.KEYDOWN:
            # to work wih one key
            if event.key == pygame.K_SPACE:
                print("jump")
        # print true when any key is realised
        # if event.type == pygame.KEYUP:
        #     print("key up")
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect, width=10)  # just use hexacolor for test we can use rgb also
    pygame.draw.rect(screen, '#c0e8ec', score_rect)

    screen.blit(score_surf, score_rect)
    snail_rect.left -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)

    # key input get by pygame.key.get_pressed
    # help to get a list of 0, 1 where 0 is false and 1 is true
    # if key is pressed it will append 1 and if not it will append 0
    # Keys = pygame.key.get_pressed()
    # by pygame.K_ we can get all keys info in 1, 0
    # if Keys[pygame.K_SPACE]:
    #     print("Jump")

    pygame.display.update()
    clock.tick(60)