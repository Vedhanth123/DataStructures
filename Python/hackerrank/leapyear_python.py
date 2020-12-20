
year = 1800

check = False

if(year % 4 == 0):

    check = True
    if(year % 100 == 0):
        
        check = False
        if(year % 400 == 0):

            check = True


print(check)
        