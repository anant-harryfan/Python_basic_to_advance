import time
from gtts import gTTS
import pygame

text = ["one", "two", "three", "four", "five", "six", 'seven', "eight", "nine", "ten", "eleven", "twelve", 'thirteen', "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty", "thirty one", "thirty two", "thirty three", "thirty four", "thirty five", "thirty six", "thirty seven", "thirty eight", "thirty nine", "forty", "forty one", "forty two", "forty three", "forty four", "forty five", "forty six", "forty seven", "forty eight", "forty nine", "fifty", "fifty one", "fifty two", "fifty three", "fifty four", "fifty five", "fifty six", "fifty seven", "fifty eight", "fifty nine", "sixty", "sixty one", "sixty two", "sixty three", "sixty four", "sixty five", "sixty six", "sixty seven", "sixty eight", "sixty nine", "seventy", "seventy one", "seventy two", "seventy three", "seventy four", "seventy five", "seventy six", "seventy seven", "seventy eight", "seventy nine",       "eighty", "eighty one", "eighty two", "eighty three", "eighty four", "eighty five", "eighty six", "eighty seven", "eighty eight", "eighty nine", "ninety", "ninety one", "ninety two", "ninety three", "ninety four", "ninety five", "ninety six", "ninety seven", "ninety eight", "ninety nine", "Hundred"]

path = fr"C:\Users\xyz\PycharmProjects\PythonTuts\Python_Project_By_Me\AI_Karate_Trainer\Resources_Karate\Audio\99.mp3"
t = 0
while t != 40:
    time.sleep(5)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

