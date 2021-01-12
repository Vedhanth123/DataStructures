strings = []
for x in range(0,2):

    string = input()
    strings.append(string)


print(strings)

y = 0
while (y < len(strings)):

    even_string = ""
    odd_string = ""
    string = strings[y]
    x = 0
    while(x < len(string)):
        if(x % 2 == 0):
            even_string += string[x]
            
        else:
            odd_string += string[x]
            
        x += 1
    y += 1
    print(even_string + "  " + odd_string)
