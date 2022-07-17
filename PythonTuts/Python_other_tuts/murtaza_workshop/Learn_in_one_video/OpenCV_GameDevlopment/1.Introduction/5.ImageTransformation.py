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
# pygame.transform.rotate help to rotate img, where 90 is angle
# imgBalloonRed = pygame.transform.rotate(imgBalloonRed, 90)
# pygame.transform.rotozoom() help to rotate img smoothly without blur ness, we can give scale also
imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 0, 1)
# pygame.transform.flip(img, want_to_flip_x_bool, want_to_flip_y_bool) help to flip img,
# imgBalloonRed = pygame.transform.flip(imgBalloonRed, True, True)

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
    # pygame.transform.scale(img, size) help to scale img
    # imgBalloonRed = pygame.transform.scale(imgBalloonRed, (50, 100))
    # pygame.transform.smoothscale() help to scale img without blur ness (recommended)
    imgBalloonRed = pygame.transform.smoothscale(imgBalloonRed, (50, 100))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
