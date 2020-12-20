# python program to automate log making

# importing datetime module to print date
from datetime import datetime

print("What did you learn today : ")

# initializing list of actions done
liset = []

# appending actions to list
while(True):

    string = input()
    if(string == ""):
        break
    liset.append(string)

# opening and writing actions done to a file
with open("/home/vedhanth/Documents/Logs/log.txt", "a+") as fp:

    fp.write(f"\n{datetime.now()}:\n")
    fp.write(f"  I've learned/learned to do/practiced:\n\n")
    y = 1
    for x in liset:

        fp.write(f"   {y}) {x}\n")
        y += 1
