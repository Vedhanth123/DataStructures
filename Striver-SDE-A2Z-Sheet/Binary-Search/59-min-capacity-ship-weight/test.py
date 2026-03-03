
mid = 8
weights = [1,2,3,4,5,6,7,8,9,10]


daysToShip = 1
remWeight = mid
for weight in weights:  
    print(f"remWeight = {remWeight}, daysToShip = {daysToShip}, weight = {weight}",end=" | ")
    if(remWeight - weight < 0):
        daysToShip += 1
        remWeight = mid
        if(remWeight > weight):
            daysToShip = float('inf')
            break
        remWeight -= weight
    else:
        remWeight -= weight
    print(f"remWeight = {remWeight}, daysToShip = {daysToShip}")