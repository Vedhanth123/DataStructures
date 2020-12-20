# number guess game
num=18
i=1
while(i<=5):
    a=int(input("Enter any no. between 1-25 :\n"))
    if(num==a):
        print("Congratulations you won the game your no. of tries you took are :",i)
        break
    else:
        if(i==5):
            print("Sorry no. of guesses have finished :\nGAME OVER :")
        else:
            if(num<a):
                print("You are ahead of the number try again : No. of tries left are ",5-i)
            if(num>a):
                print("You are behind of the number try again : No. of tries left are ",5-i)
    i+=1

        

        

    