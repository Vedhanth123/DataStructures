# problem from hacker rank to calculate sum of hour glass
# and returning which hour glass has the maximum value

arr = [[1 ,1 ,1 ,0 ,0 ,0],
       [0 ,1 ,0 ,0 ,0 ,0],
       [1 ,1 ,1 ,0 ,0 ,0],
       [0 ,0 ,2 ,4 ,4 ,0],
       [0 ,0 ,0 ,2 ,0 ,0],
       [0 ,0 ,1 ,2 ,4 ,0]]

# array to store all the values of hour glasses in array
sumed = []

# looping through the array and calculating the sum of hour glass
for i in range(len(arr)-2):

    for j in range(len(arr)-2):

        sumed.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        
# sorting the array and printing out the largest value of the array
sumed.sort()
print(sumed[-1])    