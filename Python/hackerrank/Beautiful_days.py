# Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number , its reverse is . Their difference is . The number  reversed is , and their difference is .

# She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

# Given a range of numbered days,  and a number , determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where  is evenly divisible by . If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.


# 1) reverse each number in the following range
# 2) find the absolute difference between the number and the reverse of number
# 3) divide the difference by the divisor
# 4) check if the value is a whole number and append those values to an array
# 5) print number of values in the array


# 1) reverse each number

def reverse(number):

    reverse_number = 0
    while (number != 0):

        remainder = number % 10
        reverse_number = reverse_number * 10 + remainder
        number = number // 10
    
    return reverse_number

# 2 and 3) finding absolute difference and dividing by divisor

def divided_day(number, reversed_number,divider):

    return abs(number - reversed_number)/divider


# 4) check if number is whole or not and appending those values to an array
numbers_which_are_whole = []

def whole_number_checker(number):

    number = number * 10

    remainder = number % 10

    if(remainder == 0):
        numbers_which_are_whole.append(number*10)

def beautifulDays(i, j , k):

    for x in range(i, j+1):

        # 1) reverse each number in the following range
        reversed_number = reverse(x)
        
        # 2 and 3) finding absolute difference and dividing by divisor
        divided_number = divided_day(x, reversed_number,k)

        # 4) check if number is whole or not and appending those values to an array

        whole_number_checker(divided_number)

        # 5) print number of values in the array

    print(len(numbers_which_are_whole))

beautifulDays(13 ,45, 3)

