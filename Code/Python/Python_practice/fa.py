# python program to add factorials 

def solution():

    summer = 0

    for x in range(1,13):
        
        
        def factorial(number):
            if(number == 1):
                return number
            else:
                return number * factorial(number - 1)

        summer += factorial(x)

    print(summer)

solution()