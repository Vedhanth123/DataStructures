# Program on decorators without syntactic sugar but using some example

# This program prints whee if the time is in between 7 am to 9 pm

# importing datetime for knowing time of execution
from datetime import datetime

# function (parent) runs the inner function which checks whether it is correct time
def not_during_the_night(func):

    # inner function to check time and execute function which prints whee if
    # the requested time is right
    def wrapper():
        if 7 <= datetime.now().hour < 21:
            func()
        else:
            print("  Hush, the neighbors are asleep ")

    # returning inner function to run that function outside of this function
    return wrapper

# function to print whee
def say_whee():
    print("Whee!")

# running function along with giving the argument "say_whee" function
# then "assigning not_during_the_night" to say_whee()
say_whee = not_during_the_night(say_whee)

# executing say_whee (it contains not_during_the_night methods in it)
say_whee()

# same function and decoration with syntactic sugar
@not_during_the_night
def say_whee1():
    print("whee!")

say_whee1()

# decorator with arguments in wrapper using decorators

# parent function to run inner function
def function(func):

    # function which prints random numbers and takes n arguments as function class
    def wrapper(*args):
        print("hello")
        func(*args)
        print("how are you!")
    return wrapper

# using decoration with syntactic sugar along with giving arguments to decoration
@function
def function1(num):
    print(num)

function1(14)

