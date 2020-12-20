# python program to determine palindromes using recursive approach

# algorithm:

# 1) If a string has only one letter or no letters then the string is a palindrome
# 2) If a string has two or more letters then check whether the first and last letters are same
# 3) If not then the string is not a palindrome
# 4) If then strip down the last letters and check the inner letters 
# 5) Repeat the step 4 untill there are no or only one letter left

def palindrome_recursive_approach(p):

    if(len(p) == 1 or len(p) == 0):
        
        print(True)
        
    else:

        if(p[0] == p[len(p)-1]):
            palindrome_recursive_approach(p[1:len(p)-1])
        else:
            print(False)

palindrome_recursive_approach("121")