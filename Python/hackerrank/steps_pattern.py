# hackerrank problem to print
"""
    #
   ##
  ###
 ####
#####
"""

n = 6
for x in range(1,n):

    for y in range(1,n-x):

        print(" ", end="")
    
    for z in range(x):

        print("#",end="")

    print("")