"""
Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given  queries in the form of , , and  representing the respective positions for cats  and , and for mouse . Complete the function  to return the appropriate answer to each query, which will be printed on a new line.

If cat  catches the mouse first, print Cat A.
If cat  catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

"""

def catAndMouse(x, y, z):
    

    dist_of_cat1 = abs(y-x)
    dist_of_cat2 = abs(z-y)

    print(dist_of_cat1,dist_of_cat2)
    if(dist_of_cat1 == dist_of_cat2):
        return ("Mouse C")
    elif(dist_of_cat1 > dist_of_cat2):
        return ("Cat B")
    else:
        return ("Cat A")

print(catAndMouse(1,2,3))