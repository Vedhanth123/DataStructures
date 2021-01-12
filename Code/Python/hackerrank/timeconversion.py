# python program to solve time conversion problem in hackerrank

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM
# on a 12-hour clock, and 12:00:00 on a 24-hour clock.


def timeConversion(s):


    if(s[:2] == "12" and s[len(s)-2:] == "PM"):
        return ( str(int(s[:2])) + s[2:len(s)-2])

    elif(s[:2] == "12" and s[len(s)-2:] == "AM"):
        return ( str(int(s[:2]) - 12) + s[2:len(s)-2])

    elif(s[len(s)-2:] == "PM"):
        return ( str(int(s[:2]) + 12) + s[2:len(s)-2])

    elif(s[len(s)-2:] == "AM"):
        return ( str(int(s[:2])) + s[2:len(s)-2])


print (timeConversion("07:00:00AM"))














