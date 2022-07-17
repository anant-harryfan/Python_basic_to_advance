# Import
import time
import pygame
from numpy import rot90
import cv2
import pyttsx3

# setting up pyttsx3 help to make computer speck
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 100)
engine.setProperty('rate', 200)
def speck(audio):
    """ Help to computer to speck """
    engine.say(audio)
    engine.runAndWait()
    # engine.stop()
fileN = -1
def countt(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

# Music
# music_dir = 'C:\\Users\\xyz\\OneDrive\\Desktop\\songs'
# songs = os.listdir(music_dir)
# rand = random.randint(0, len(songs) - 1)

# Variable
countF = 00
count = 0
totalTime = 10
startTime = time.time()

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
            exit()

    # Apply Logic
    timeRemain = int(totalTime - (time.time() - startTime))
    # print(timeRemain)
    # opencv
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    window.blit(frame, (0, 0))
    if timeRemain <= 0:
        if count < 100:
            font = pygame.font.Font("./Resources_Karate/Marcellus-Regular.ttf", 150)
            pygame.draw.rect(window, (0, 255, 0), (58, 457, 345, 220), border_radius=50)  # border radius css wala
            countF += 1
            showCount = font.render(f'{count}', True, (50, 50, 255))
            if countF == 25:
                countF = 0
                count += 1
                fileN += 1
                if fileN != 101:
                    path = fr"C:\Users\xyz\PycharmProjects\PythonTuts\Python_Project_By_Me\AI_Karate_Trainer\Resources_Karate\Audio\{fileN}.mp3"
                    countt(path)

            window.blit(showCount, (150, 470))
        elif count >= 100:
            font = pygame.font.Font("./Resources_Karate/Marcellus-Regular.ttf", 50)
            pygame.draw.rect(window, (255, 0, 0), (250, 207, 845, 220), border_radius=20)  # border radius css wala
            TotalPunch = font.render(f'You completed all 100 punches', True, (50, 50, 255))
            window.blit(TotalPunch, (300, 270))
    else:
        pygame.draw.rect(window, (0, 255, 175), (250, 237, 770, 220), border_radius=20)  # border radius css wala
        font = pygame.font.Font("Resources_Karate/Marcellus-Regular.ttf", 50)
        textTime = font.render(f'Training Starts in: {timeRemain}', True, (50, 50, 255))
        window.blit(textTime, (400, 305))


    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)


