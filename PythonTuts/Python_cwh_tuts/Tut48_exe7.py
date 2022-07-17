from pygame import mixer
from time import time
import time
def alarm(file, stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stoper:
            mixer.music.stop()
            break

def logFile(mes):
    with open("tut48_logs", "a") as log:
        log.write(f"{mes} at {time.asctime(time.localtime(time.time())) } \n")


def idk(init_, sec_, mes_, stopper_, music_file, log_):
    if time.time() - init_ > sec_:
        print(f"{mes_}. Enter \'{stopper_}\' to stop the alarm")
        alarm(music_file, stopper_)
        time.sleep(water_sec)
        logFile(log_)

if __name__ == '__main__':
    init_water = time.time()
    # init_eyes = time.time()
    # init_workout = time.time()
    water_sec = 30*60
    # eye_sec = 2
    # workout_sec = 4

    while True:
        idk(init_water, water_sec, "Drink water now", "drank", "tut48_water.mp3", "Last time you drink water at - ")