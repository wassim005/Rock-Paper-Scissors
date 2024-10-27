import random

rounds = 0
playerPoints = 0
cpuPoints = 0

def game():
    global playerPoints, cpuPoints
    if is_draw(user, opponent):
        print("It's a draw!")
    elif is_win(user, opponent):
        playerPoints += 1
        print("You won this round!")
    elif is_lose(user, opponent):
        cpuPoints += 1
        print("CPU won this round!")
    print("The score is", playerPoints, "-", cpuPoints)
    print("===========================================")

def is_win(user, opponent):
    return (user == "r" and opponent == "s") or (user == "s" and opponent == "p") or (user == "p" and opponent == "r")

def is_lose(user, opponent):
    return (opponent == "r" and user == "s") or (opponent == "s" and user == "p") or (opponent == "p" and user == "r")

def is_draw(user, opponent):
    return user == opponent

while rounds < 3:
    user = input("'r' for Rock 'p' for Paper 's' for Scissors, What's your choice? ")
    opponent = random.choice(["r", "p", "s"])
    print(f"CPU chose: {opponent}")
    rounds += 1
    game()
    


print("===========================================")
print("Final score:", playerPoints, "-", cpuPoints)
if playerPoints > cpuPoints:
    print("You won the game!")
elif cpuPoints > playerPoints:
    print("CPU won the game!")
else:
    print("The game is a draw!")
print("===========================================")
print("===========================================")