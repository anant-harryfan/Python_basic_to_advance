import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
clock = pygame.time.Clock()
sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()
test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)
# we can use pygame color or our customize color
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
        # get pos when mose move
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            x, y = event.pos
        # get pos when mouse button is down
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("down")
        # get pos when mouse button is up
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("up")
        # get pos when we scroll
        # if event.type == pygame.MOUSEWHEEL:
        #     print("wheel")
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # help to draw rect, pygame.draw used to draw other things also
    # surface, color, (x,y,w,h), (draw only width, no center wil be draw), boarder radius
    pygame.draw.rect(screen, '#c0e8ec', score_rect, width=10)  # just use hexacolor for test we can use rgb also
    pygame.draw.rect(screen, '#c0e8ec', score_rect)

    screen.blit(score_surf, score_rect)
    snail_rect.left -= 4
    if snail_rect.left <= -100:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    # player_rect.left += 1
    screen.blit(player_surf, player_rect)

    # collide rect is recommended on collide point
    # player_rect.colliderect(snail_rect) help to detect that rect is colliding with given rect
    # if player_rect.colliderect(snail_rect):
    #     print("colliding")
    # player_rect.collidepoint((x, y))  help to get that if rect collide with a certain point
        # doing it using mouse point by pygame.mouse  # recommended
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

        # using event loop for mouse   # not recommended
    # if player_rect.collidepoint((x, y)):
    #     print("collide")
    # help to draw line
    # pygame.draw.line(surface=screen, color='black', start_pos=(0, 0), end_pos=pygame.mouse.get_pos(), width=10)
    pygame.display.update()
    clock.tick(60)