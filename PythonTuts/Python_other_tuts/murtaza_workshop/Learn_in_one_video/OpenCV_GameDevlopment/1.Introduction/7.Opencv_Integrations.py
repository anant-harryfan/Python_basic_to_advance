# Import
import pygame
import cv2
import numpy as np

# Initialize
pygame.init()

# create window or display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome project")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# WebCam
cap = cv2.VideoCapture(0)

# Main loop
start = True
while start:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
        # opencv
    success, img = cap.read()
    img = cv2.resize(img, (1380, 720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
