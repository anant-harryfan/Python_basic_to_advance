import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))  # default color is black
pygame.display.set_caption("PygameAwesome")
clock = pygame.time.Clock()
# use to make surface on screen, where 100 is width and 200 is height
# creates a surface
# test_surface = pygame.Surface((100, 200))  # default color is black
# test_surface.fill("red")  # help to fill surface with a color

sky_surface = pygame.image.load("Resources/graphics/Sky.png").convert_alpha()  # to load a img
ground_surface = pygame.image.load("Resources/graphics/ground.png").convert_alpha()  # convert help to process img faster in pygame
# to create a text first we need to convert it into img
# help to create font for a text, where font type is 1st argument (if not want can be none), 2nd argument is size
test_font = pygame.font.Font("Resources/font/Pixeltype.ttf", 50)
# load text, 1st argument = text, 2nd argument = smoothness, 3 argument - color
text_surface = test_font.render("Score", False, 'Black')
snail_surface = pygame.image.load("Resources/graphics/snail/snail1.png").convert_alpha()  # to get a transparent img
snail_x_pos = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # help to blit things from surface to surface
    # screen.blit()
    # sky_surface is regular surface, (0, 0) is (x, y) pos
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 265))
    # the sequence for bliting a img is imp otherwise you will not able to see img
    pygame.display.update()
    clock.tick(60)