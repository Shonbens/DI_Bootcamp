from random import randint

win = 0
loss = 0
draw = 0

# create a list of play options
t = ["rock", "paper", "scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]

while True:
    player = input("rock, paper, scissors? Type x to quit")
    winning = f"You chose: {player}, computer chose: {computer} Result: W"
    loosing = f"You chose: {player}, computer chose: {computer} Result: L"
    drawing = f"You chose: {player}, computer chose: {computer} Result: draw"
    if player == computer:
        print(drawing)
        draw += 1
        player = False
    elif player == "rock":
        if computer == "paper":
            print(loosing)
            loss += 1
            player = False
        else:
            print(winning)
            win += 1
            player = False
    elif player == "paper":
        if computer == "scissors":
            print(loosing)
            loss += 1
            player = False
        else:
            print(winning)
            win += 1
            player = False
    elif player == "scissors":
        if computer == "rock":
            print(loosing)
            loss += 1
            player = False
        else:
            print(winning)
            win += 1
            player = False
    elif player == "x":
        print(f"you won {win} times")
        print(f"you lost {loss} times")
        print(f"you drew {draw} times")
        print("thanks for playing!")
        break
    else:
        print("incorrect type")
        player = False

    computer = t[randint(0, 2)]
