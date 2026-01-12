'''
3
100
101 100 304
100 1 200
'''

# testCases = int(input("No of testcases: "))
# intitalPower = int(input("Initial Power: "))
# powerRequired = list(map(lambda x: int(x), input("Power required: ").split(' ')))
# bonusGranted = list(map(lambda x: int(x), input("Bonus earned: ").split(' ')))
import heapq

testCases = 3
intitalPower = 100
powerRequired = [101, 100, 304]
bonusGranted = [100, 1, 200]

newArray = []


for x in range(testCases):

    newArray.append((powerRequired[x], bonusGranted[x]))

heapq.heapify(newArray)
answer = 0
while(True):
    
    powerReq, bonusGrant = heapq.heappop(newArray)
    if(powerReq <= intitalPower):    
        intitalPower += bonusGrant
        answer += 1
    else:
        break

print(answer)

