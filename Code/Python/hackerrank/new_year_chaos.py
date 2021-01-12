def minimumBribes(q):

    array = q
    total_no_of_bribes = 0
    # looping through array from index '1'
    for x in range(1, len(array)):

        # storing a value to be checked if it is sorted
        key = array[x]

        # creating an invariable
        i = x - 1

        no_of_bribes = 0
        # checking if it is sorted if not then keeping it in the correct place
        while ((key < array[i]) and (i >= 0)):

            if(no_of_bribes > 2):
                return "Too chaotic"
            
            total_no_of_bribes += 1
            # swapping till the key gets to its proper place
            array[i+1], array[i] = array[i], array[i+1]
            i -= 1
            no_of_bribes += 1
        
    return total_no_of_bribes

print(minimumBribes([5, 1, 2, 3, 7 ,8 ,6 ,4]))