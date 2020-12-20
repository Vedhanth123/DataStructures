# program to print fibonacci series to n

limiter = int(input("Enter limit : "))


post_num = 1
pre_num = 0
num_to_be_printed = 0

def fibonacci(post_num,pre_num,num_to_be_printed,limiter):

# """          
#  Description: 
#     This function prints out fibonacci series 
 
#  Algorithm:
#     1, (1+0) -> 1, (1+1) ->  2, (1+2) ->  3, (2+3) ->  5......

# """

   for x in range(1, limiter):

      print(num_to_be_printed)
      num_to_be_printed = pre_num + post_num
      
