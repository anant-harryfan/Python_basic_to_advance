"""
Rect

    Can detect Collisions
    Can access x and y points

    Two ways of creating a rect
    1. pygame.Rect(x, y, width, height)
    2. surface.get_rect()  # creates rect around a surface/image
"""

# Import
import pygame

# Initialize
pygame.init()

# create window or display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome project")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Loading Images
# to get jpg image, convert help to process img faster in pygame
imgBackground = pygame.image.load("./0.Resources_GameDev/BackgroundBlue.jpg").convert()
# to get png image, convert help to process img faster in pygame
imgBalloonRed = pygame.image.load("./0.Resources_GameDev/BalloonRed.png").convert_alpha()
# help to make rectangle in background of an img (here img is imgBalloonRed)
RectBalloon = imgBalloonRed.get_rect()

# Rect
# create a rectangle
rectNew = pygame.Rect(500, 0, 200, 200)
# Main loop
start = True
while start:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    # if we want to see collide between two rectangle
    print(RectBalloon.colliderect(rectNew))
    # to change position for the rectangle of img
    RectBalloon.x += 5
    # RectBalloon.y += 5
    # to change position of rect we created
    # rectNew.x += 5
    # rectNew.y += 5

    # blit help to add anything on window
    window.blit(imgBackground, (0, 0))
    # it create rectangle on the img
    # pygame.draw.rect(window, (0, 255, 0), RectBalloon)
    # pygame.draw.rect(window, (0, 255, 0), rectNew)
    # RectBalloon is position
    window.blit(imgBalloonRed, RectBalloon)

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
