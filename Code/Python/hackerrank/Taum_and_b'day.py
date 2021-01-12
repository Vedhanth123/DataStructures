# Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

# The cost of each black gift is  units.
# The cost of every white gift is  units.
# The cost to convert a black gift into white gift or vice versa is  units.
# Determine the minimum cost of Diksha's gifts.


# 1) compare the price of each gifts
# 2) if the price of white gifts is greater than the price of black gifts and z units '
#    buy all black gifts and change them to white gifts

# 3) else vice versa

def taumBday(b, w, bc, wc, z):

    if(bc > wc + z):

        white_gifts_price = wc * w
        black_gifts_price = (wc + z) * b
        total_price = white_gifts_price + black_gifts_price
        return total_price

    elif(wc > bc + z):
        black_gifts_price = bc * b
        white_gifts_price = (bc + z) * w
        total_price = white_gifts_price + black_gifts_price
        return total_price

    else:
        black_gifts_price = bc * b
        white_gifts_price = wc * w
        total_price = white_gifts_price + black_gifts_price
        return total_price
    
print(taumBday(3,3,1,9,2))

        


    
    