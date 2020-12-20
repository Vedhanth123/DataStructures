# program to solve hacker rank problem of rounding student grade problem

def rounder(number):

    multiple = (number // 5) + 1
    if(((multiple * 5) - number) < 3):
        number = multiple * 5
        return number
    else:
        return number


