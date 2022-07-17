import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
clock = pygame.time.Clock()
sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()
test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)
text_surface = test_font.render("Score", False, 'Black')
snail_surface = pygame.image.load("Resources/graphics/snail/snail1.png").convert_alpha()
# snail_x_pos = 600
snail_rect = snail_surface.get_rect(midbottom=(680, 300))
player_surf = pygame.image.load("Resources/graphics/Player/player_walk_1.png").convert_alpha()
# player_rect = pygame.Rect(left, top, width, height)  # we can give val
# or we can just get img size and draw rect like this
# argument # not req = topLeft, topRight, topMid, bottomLeft, bottomRight, bottomMid, midRight, midLeft, center  # all letters are in small case in function
player_rect = player_surf.get_rect(midbottom=(80, 300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    snail_rect.left -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    # to move object from the given point
    player_rect.left += 1
    screen.blit(player_surf, player_rect)
    pygame.display.update()
    clock.tick(60)