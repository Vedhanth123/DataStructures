# python program to implement palindrome in python

def palindrome_checker(string):

    # looping through array

    for x in range(len(string)//2):

        # if first and last element of string are not alike
        if(string[x] != string[(len(string)-1)-x]):
            return "not a palindrome"

        # then checking second and second last elements
        # this runs till string is finished

    return "palindrome"


print(palindrome_checker("madam"))
