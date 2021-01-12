""" Program to keep the programmer healthy 
    reminds to drink water every 15 min
    reminds to exercise every 30 min
    reminds to give rest to eye every 45 min
"""

# importing pygame and time module to play audio and calculate time
from pygame import mixer
import time

# function to play audio
def musiconloop(file, stopper):  # function to play music on loop
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

# function to write log of water drank, exercised
def log(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {time.asctime(time.localtime())}\n")

# code which will not be executed if it is imported to another program
if __name__ == "__main__":

    initial_time_water = time.time()
    initial_time_eye = time.time()
    initial_time_exer = time.time()
    waterseconds = 600
    eyeseconds = 1200
    exerseconds = 1800

    # looping and checking time and playing audio if time reaches the required time
    while True:
        if time.time() - initial_time_water > waterseconds:
            print("Water drinking time : ")
            musiconloop("goo.ogg","drank")
            initial_time_water = time.time()
            log("Drank water at Enter \"drank\" to stop ")

        if time.time() - initial_time_eye > eyeseconds:
            print("eye time : ")
            musiconloop("goo.ogg","eyedone")
            initial_time_eye = time.time()
            log("Eyes excercised at Enter \"eyedone\" to stop ")

        if time.time() - initial_time_exer > exerseconds:
            print("Exer time : ")
            musiconloop("goo.ogg","exerdone")
            initial_time_exer = time.time()
            log("Done activity at Enter \"exerdone\" to stop ")
