import random
print("Welcome! to the ROCK PAPER SCISSORS GAME :  ")
print("Press 'r' for rock 'p' for paper 's' for scissor :  ")
print("Please Enter the input ")

computer_score = 0
user_score = 0


def Game(computer_score, user_score):

    lchoice = ("rock", "paper", "scissors")
    cchoice = random.choice(lchoice)
    choice = input("Enter the choice : ")
    if(choice == "r"):
        if(cchoice == "rock"):
            print("Draw match :")
        elif(cchoice == "scissor"):
            print("You won the game :")
            user_score = user_score + 1
        else:
            print("You lost the game :")
            computer_score = computer_score + 1
    if(choice == "p"):
        if(cchoice == "paper"):
            print("Draw match :")
        elif(cchoice == "rock"):
            print("You won the game :")
            user_score = user_score + 1
        else:
            print("You lost the game :")
            computer_score = computer_score + 1
    if(choice == "s"):
        if(cchoice == "scissor"):
            print("Draw match :")
        elif(cchoice == "paper"):
            print("You won the game :")
            user_score = user_score + 1
        else:
            print("You lost the game :")
            computer_score = computer_score + 1
    print("To continue the game press 1 and to exit the game press 0 :")
    n = int(input())
    if(n == 0):
        print("Scores are : computer = ", computer_score, " user = ", user_score)
        return 0
    else:
        Game(computer_score, user_score)


Game(computer_score, user_score)
