import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PygameAwesome")
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)




# import pygame
# # to safely exit from our code
# from sys import exit
# pygame.init()  # help to use pygame, without using this you can't do anything
# # use to make screen, where 800 is width and 400 is height
# screen = pygame.display.set_mode((800, 400))
# pygame.display.set_caption("PygameAwesome")
# clock = pygame.time.Clock()
# # when we just use code till this it will show one frame and end
# while True:  # by this we can get frame forever
#     # to get all event we use pygame.event.get()
#     for event in pygame.event.get():
#         # Get info that user want to exit the program
#         if event.type == pygame.QUIT:
#             # use to quit from code
#             pygame.quit()  # it is opposite of pygame.init(), pygame.init() - initialize code, pygame.quit() - uninitialized code
#             exit()  # we can use break but it will create some problem
#     pygame.display.update()  # help to update our screen to perform as our code says
#     clock.tick(60)  # tells the while true to not run more that 60 fps
