
# 1) check if the year is same
# 2) check if the month is same
# 3) check if the date is less than or equal to the due date


def libraryFine(d1, m1, y1, d2, m2, y2):

    # 1) check if the year is same
    if(y1 > y2):
        return 10000
    
    if(m1 > m2):
        return 500 * (m1-m2)
    
    if(d1 > d2):
        return 15 * (d1-d2)
    
    if(d1 <= d2):
        return 0

print(libraryFine(9, 6, 2015,6, 6, 2015))


