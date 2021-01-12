
"""
You have been asked to help study the population of birds migrating across the continent.
Each type of bird you are interested in will be identified by an integer value.
Each time a particular kind of bird is spotted, its id number will be added to your array of sightings.
You would like to be able to find out which type of bird is most common given a list of sightings.
Your task is to print the type number of that bird and if two or more types of birds are equally common,
choose the type with the smallest ID number.

For example, assume your bird sightings are of types .
There are two each of types  and , and one sighting of type .
Pick the lower of the two types seen twice: type .
"""

# given an integer of array print out which number is recurring 
# print out which lowest number is recurring.

# def counting_recurring_numbers(array):

def counting_recurring_numbers(array,number_of_inputs):

    counter = [x-x for x in range(number_of_inputs+1)]
    for i in array:
        counter[i] += 1

    return counter

# function to find out which block of array has largest number
def counting_birds(array):

    largest = 0
    for i in range(len(array)):
        if(largest < array[i]):
            largest = array[i]
        
    # looping to find out which lowest block has largest number
    for j in range(len(array)):
        if(largest == array[j]):
            return j

array = counting_recurring_numbers([1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1, 3 ,4],5)
print(array)    
print(counting_birds(array))
