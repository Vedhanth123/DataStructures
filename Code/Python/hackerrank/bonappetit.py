"""
Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally.
Brian wants to order something that Anna is allergic to though,
and they agree that Anna won't pay for that item.
Brian gets the check and calculates Anna's portion.
You must determine if his calculation is correct.

"""


def bon_appetit(array,brian,bill_payed):

    # inner function to calculate bill 
    def bill(array):
        sumed = 0
        for x in range(len(array)):
            sumed += array[x]

        return sumed
    
    # removing element which anna did not eat
    array.pop(brian)

    # calculating the bill after excluding the disk anna did not eat
    popped_sum = bill(array)

    # if bill payed is equal to the excluded bill then print bon appetit    
    if(popped_sum//2 == bill_payed):
        print( "bon_appetit")
        
    # else print amount of money brian owes anna 
    else:
        print(bill_payed-popped_sum//2)

bon_appetit([3, 10, 2, 9],1,7)