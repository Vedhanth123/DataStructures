# This is the first introduction video of the counter

# let's use global variables for this case
count = 0
def rec():

    global count
    if(count == 3):
        return
    print(count)
    count += 1;
    rec()

rec()
