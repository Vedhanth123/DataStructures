"""Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, and Dan has a maximum height he can jump. There is a magic potion he can take that will increase his maximum height by  unit for each dose. How many doses of the potion must he take to be able to jump all of the hurdles.

Given an array of hurdle heights , and an initial maximum height Dan can jump, , determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race
"""

def hurdleRace(k, height):

    maximux_value_in_array = 0
    for x in range(len(height)):
        if(maximux_value_in_array < height[x]):
            maximux_value_in_array = height[x]

    if(k < maximux_value_in_array):
        return maximux_value_in_array - k
    else:
        return 0

print(hurdleRace(7,[2,4,5,4,5,2]))