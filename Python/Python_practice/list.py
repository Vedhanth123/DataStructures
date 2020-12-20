'''
# Problem from hacker rank to solve Jumping on Clouds
def jumpingOnClouds(c):

    i = counter = 0
    while(i < len(c)):
        
        try:
            if(c[i+2] or (i == (len(c) - 2))):
                i += 1
                counter += 1
        except:
            
            counter += 1
            break

        
        else:
            i += 2
            counter += 1

    
    print (counter)

c = [0,0,0,1,0,0]

jumpingOnClouds(c)
'''

# experimenting on remove function in list

array = [1,0,0,0,0, 2]
array.remove(0)
print(array)