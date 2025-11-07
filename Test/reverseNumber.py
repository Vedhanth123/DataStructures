'''
1) Pick the right most digit of the number and append that to the new number
2) To pick the right most digit of the number (number in unit's place) use % 10
3) To apppend the the rem to a new number the multiply the new number by 10 and add the rem to the new number 
'''

num = int(input())

rev = 0

while(num):
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

print(rev)

'''
Time Complexity: O(n)
space complexity: O(1)
'''