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
# to get png image, convert_alpha help to process img faster in pygame and use to get transparent background - can be used in jpg images also
imgBalloonRed = pygame.image.load("./0.Resources_GameDev/BalloonRed.png").convert_alpha()

# Main loop
start = True
while start:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    # blit help to add anything on window
    window.blit(imgBackground, (0, 0))
    # (100, 100) is position
    window.blit(imgBalloonRed, (100, 100))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
