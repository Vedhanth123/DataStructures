# program to find no_of_duplicates in an array 


lister = [11,100,94,97,10,6,3,9,1,2,6,8,9,10,100,100,943,4,5,7,1]
no_of_duplicates = 0
    
iterator = 0
var = lister[0]
while (iterator <= 100):
    if (var == lister[iterator]):
       no_of_duplicates += 1
       iterator += 1
       if (iterator >= len(lister)):
           if no_of_duplicates!= 0:
               print(f"no. of no_of_duplicates of {var} are {no_of_duplicates}")
       break        
    
    else:
        if (no_of_duplicates != 0):
            print(f"no. of no_of_duplicates of {var} are {no_of_duplicates}")
        var += 1
        no_of_duplicates = 0
        if (iterator > len(lister)-1):
            break


            


        
        
        

