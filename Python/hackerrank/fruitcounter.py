# program to solve apple and orange problem from hacker rank

def fruit_counter(s, t, a, b, apples, oranges):

    no_of_oranges = no_of_apples = 0

    for app in apples:
        if(s <= (app + a) <= t):
            no_of_apples += 1
    
    for ora in oranges:
        if(s <= (ora + b) <= t):
            no_of_oranges += 1
    print(f"{no_of_oranges}\n{no_of_apples}")

fruit_counter(7 ,11,5 ,15,[-2,2,1],[5,-6])
        

