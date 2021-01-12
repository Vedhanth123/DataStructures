# python program to implement pattern

   #
  ###
 #####
#######
 #####
  ###
   #
    
def pattern(height):
    iterator = iterator2 = 0

    while(iterator != (height*2)-1):

        while(iterator2 < height-iterator):
            
            print(" ",end="")
            iterator2+=1

        print("#")
        iterator+=1


pattern(4)