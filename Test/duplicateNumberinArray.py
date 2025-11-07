'''
1) to Find duplicate numbers in an array we use HashMaps (dictionaries in python)
2) find the frequencies of the numbers in an array and store them in hashMap
3) Iterate through the hashMap and find out whose value is greater than 1. 
4) Put then in an array (answer)
5) return that array
'''

answer = []

freq = {}

array = [1,2,2,3,7,2,3,9,0,1]

for x in range(len(array)):
 
    if(array[x] not in freq):
        freq[array[x]] = 1
    else:
        freq[array[x]] += 1


for key, val in freq.items():
    if(val > 1):
        answer.append([key, val])

print(answer)


'''
Time Complexity: O(n)
Space Complextiy: O(n)
'''