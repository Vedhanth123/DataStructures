'''
1) Put up left and right pointers to the extremes of the string
2) Check if the the characters at the respective indicies are same
3) If not return true
4) Continue till the left < right
'''

string = "MadaM"
string2 = "Hello"


def checkPalindrome(s):
    left = 0 
    right = len(s) - 1
    while(left < right):
        if(s[left] != s[right]):
            return False
        left += 1
        right -= 1
    
    return True

print(checkPalindrome(string))
print(checkPalindrome(string2))