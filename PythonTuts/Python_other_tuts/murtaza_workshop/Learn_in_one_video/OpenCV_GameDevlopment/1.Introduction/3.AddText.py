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

# Main loop
start = True
while start:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.fill((255, 255, 255))
    # make font object, if you want to give your own font put font path in place of None 100 is size
    font = pygame.font.Font(
        '0.Resources_GameDev/Marcellus-Regular.ttf', 100)
    # it take the given text and save it in text variable, if text is blurry so make false True
    text = font.render("Jay shree ram", True, (0, 0, 0))
    window.blit(text, (350, 300))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
