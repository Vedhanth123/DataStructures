array = [1,2,3,5,4]


def sorted_or_not(x):
    
    if(x > len(array) - 2):
        return True
        
    if(array[x] < array[x+1]):
        return sorted_or_not(x+1)

    return False
    
print(sorted_or_not(0))