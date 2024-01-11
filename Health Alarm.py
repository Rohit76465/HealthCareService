from pygame import mixer
from datetime import datetime
from time import time

def Player(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inp = input()
        if inp == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("my-logs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    water_time = time()
    eyes_time = time()
    physicalexercise_time = time()

    watersecs = 5
    eyessecs = 30
    physicalexercisesecs = 60

    while True:
        if time() - water_time > watersecs:
            print("It's Water Drinking Time.\n Enter 'drank' to stop the alarm.")
            Player("water.mp3","drank")
            water_time = time()
            log_now("Drank Water at:")

        if time() - eyes_time > eyessecs:
            print("It's Eye Exercise Time.\n Enter 'doneeyes' to stop the alarm.")
            Player("eyes.mp3","doneeyes")
            eyes_time = time()
            log_now("Eyes relaxed at:")

        if time() - physicalexercise_time > physicalexercisesecs:
            print("It's Physical Activity Time.\n Enter 'doneexercise' to stop the alarm.")
            Player("physical.mp3","doneexercise")
            physicalexercise_time = time()
            log_now("Physical Activity Done at:")