def sockMerchant(n, ar):
    
    ar.sort()
    
    i = 0
    checker = ar[0]
    colours_of_sock = []
    counter = 0
    while(i < n):
        if(i == n-1):
            if(checker == ar[i]):
                counter += 1
                colours_of_sock.append(counter)
                counter = 0
                break
            else:
                colours_of_sock.append(counter)
                break


        if(checker == ar[i]):
            counter += 1
            i += 1
            
        else:
            colours_of_sock.append(counter)
            counter = 0
            checker = ar[i]
    
    
    
    print("")
    checker = 0
    for x in colours_of_sock:
        checker += x // 2
        
    
    return checker


sockMerchant(10,[1, 1, 3, 1, 2, 1 ,3 ,3, 3 ,3])
