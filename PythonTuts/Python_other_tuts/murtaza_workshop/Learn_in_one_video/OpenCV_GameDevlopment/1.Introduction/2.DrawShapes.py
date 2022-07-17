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
    # our color
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    # draws polygon    # window, color, position of all points
    pygame.draw.polygon(window, red, ((491, 100), (788, 100), (937, 357),
                                      (788, 614), (491, 614), (342, 357)))
    # draws circle    # window, color, position, radius
    pygame.draw.circle(window, green, (620, 360), 200)
                                    # start , end
    # draws line     # window, color, x1 y1, x2 y2, thickness
    pygame.draw.line(window, blue, (468, 392), (812, 392), 10)
    # draws rectangle # window. color, (x1, y1, w, h), boarder_radius
    pygame.draw.rect(window, red, (468, 307, 345, 70), border_radius=50)  # border radius css wala
    # draws arc    # window, color, rectangle,   start, end angle
    pygame.draw.arc(window, green, (50, 50, 50, 50), 45, 46)
    # create a line   # window, color, pos
    pygame.draw.aaline(window, blue, [100, 0], [700, 600])

    pygame.draw.aalines(window, green, [0, 50],[50, 890], True)

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)