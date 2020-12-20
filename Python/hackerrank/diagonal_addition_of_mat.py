array = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

var = 0
for i in range(3):

    var += array[i][i]
    var += array[i][len(array) - 1]

print(var)