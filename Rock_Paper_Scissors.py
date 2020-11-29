import sys

player1 = input("choose")
player2 = input("choose too")
def compare(u1,u2):
    if u1 == u2:
        return("its a tie")
    elif u1 == "Scissors":
        if u2 == "Rock":
            return("Rock wins!")
        else:
            return("Scissors wins!")
    elif u1 == "Rock":
        if u2 == "Paper":
            return("Paper Wins!")
        else:
            return("Rock Wins!")
    elif u1 == "Paper":
        if u2 == "Scissors":
            return("Scissors wins!")
        else:
            return("Paper wins!")
    else:
        return("invalid Input!")
        sys.exit()

print(compare(player1,player2))

