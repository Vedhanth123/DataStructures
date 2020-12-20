

array = []
for x in range(len(arr)):

    counter = 0 
    for y in range(len(arr)):

        if(y == x):

            continue    

        counter += arr[y]   
    
    array.append(counter)

array.sort()

print(array[0], array[-1])
