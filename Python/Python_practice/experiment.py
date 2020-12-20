
def function(iter,mid = 0):

    if(iter == 3):
        print(mid)
        return "0"

    else:
        iter += 1
        mid += 19
        return function(iter, mid)

print(function(0))
    