"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store.
The store has several models of each. Monica wants to spend as much as possible for the
items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget,
find and print the amount of money Monica will spend.
If she doesn't have enough money to both a keyboard and a USB drive,
print -1 instead. She will buy only the two required items.

"""

def getMoneySpent(keyboards, drives, b):

    # inserting all values which are <= b 
    All_the_values = []

    highest_value = 0
    # looping through keyboard array

    for x in range(len(keyboards)):
        
        # looping through drives array
        for y in range(len(drives)):
            
            # finding the value of this combination
            highest_value = keyboards[x] + drives[y]
        
            if(highest_value <= b):
                All_the_values.append(highest_value)
        
    # finding higest value in array
    highest_value = All_the_values[0]
    for y in All_the_values:

        if(highest_value < y):
            highest_value = y

    return highest_value

        
        

