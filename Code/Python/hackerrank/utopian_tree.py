# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after  growth cycles?

# For example, if the number of growth cycles is n = 5 , the calculations are as follows:



def utopianTree(n):

    height_of_tree = 1

    for x in range(1,n+1):
        if(x % 2):
            height_of_tree *= 2
        else:
            height_of_tree += 1
    
    return height_of_tree

print(utopianTree(4))