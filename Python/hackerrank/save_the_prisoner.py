#  jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

# The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

# 1) divide the number of chocolates by the number of seats
# 2) return absolute of starting seat - remainder


        
def saveThePrisoner(n,k,s):

    remainder = k % n

    seat = (s + remainder) - 1

    if(seat > n):
        return abs(seat - n)
    
    return seat

print(saveThePrisoner(7,19,4))