#Importing the random module
from random import randint
#possible moves
moves = ["rock" , "paper" , "scissors"]
score_user = 0
score_comp = 0

while True:
    computer = moves[randint(0,2)]
    player = input("rock,paper or scissors ? (or end the game)").lower()
    if player == "end the game":
        print("The game has been ended")
        print("Your score: ",score_user)
        print("Computer score: ",score_comp)
        break

    elif player == computer:
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
            score_comp += 1
        else:
            print("You win!" , player , "beats" , computer)
            score_user += 1

    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
            score_comp += 1
        else:
            print("You win!" , player , "beats" , computer)
            score_user += 1

    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
            score_comp += 1
        else:
            print("You win!" , player , "beats" , computer)
            score_user += 1

    else:
        print("Check your Spelling......")