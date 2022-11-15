
no_of_duplicates = {}

array1 = [1,2,3,1,2,3,3,3,3]

# we need a database to store what values are there in array
for x in range(len(array1)):
    key = array1[x]
    no_of_duplicates[key] = 0

# check how many elements are there in an array
count = 0

for x in no_of_duplicates.keys():
    
    for y in range(len(array1)):
        if(x == array1[y]):
            count+= 1
    
    no_of_duplicates[x] = count
    count = 0

# hello how are you