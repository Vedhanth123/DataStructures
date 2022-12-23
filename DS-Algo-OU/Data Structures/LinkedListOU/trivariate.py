class univariate():

    def __init__(self):
        self.data = 0
        self.powerx = 0
        self.link = None


# take a string
string = "2x^2+3x^3+4x"

terms = string.split('+')

# traverse through each term and filter out values from it
numbers = "0123456789"
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
power = "^"

head = None
tail = None

for y in range(len(terms)):

    n1 = univariate()
    n1.link = None

    n1.data = ""
    n1.powerx = "0"

    for x in range(len(terms[y])):

        if(terms[y][x] in numbers):
            n1.data += terms[y][x]
        
        if(terms[y][x] in power):
            break
    
    for z in range(x+1, len(terms[y])):
        
        n1.powerx += terms[y][z]
    
    if(head == None):
        head = n1
    else:
        tail.link = n1
    
    tail = n1


