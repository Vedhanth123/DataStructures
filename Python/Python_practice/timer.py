from pygame import mixer
import time

stopper = str(0)

# taking input time from user
sec = int(input("Enter seconds : "))
mini = int(input("Enter minutes : "))
total = sec+(60*mini)

# taking message from the user
msg = input("Enter the message to be remainded : ")

# initializing time
initialtime = int(time.time())

# initializing mixer to play audio
mixer.init()
mixer.music.load("/home/vedhanth/Documents/Python/Python_practice/ring.mp3")

# checking time every fraction of a second
while (True):
    if(time.time() - initialtime > total ):
        mixer.music.play()
        print(msg)
        stopper = input("Press any key to stop : ")
        if(0 <= ord(stopper) <= 200):
            break
    



