from random import randint

t = ["Rock", "Paper", "Scissors"]

ai = t[randint(0,2)]

p = False

while p == False:
    p = input("Rock, Paper, Scissors?")
    if p == ai:
        print("You picked the same thing, it's a tie!")
    elif p == "Rock":
        if ai == "Paper":
            print("You lose!", ai, "beats", p)
        else:
            print("You win!", p, "beats", ai)
    elif p == "Paper":
        if ai == "Scissors":
            print("You lose!", ai, "beats", p)
        else:
            print("You win!", p, "beats", ai)
    elif p == "Scissors":
        if ai == "Rock":
            print("You lose...", ai, "beats", p)
        else:
            print("You win!", p, "beats", ai)
    else:
        print("That's not a legal move. Check your spelling!")
    p = False
    ai = t[randint(0,2)]
