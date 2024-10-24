#Cecily Strong ProficiencyTest: Rock, Paper, Scissors
import random
rps=['rock','paper','scissors']
winsc=0
losesc=0
go=True
def scorecount():
    print('you have',winsc, 'points, and the computer has', losesc, 'points')
def win():
    global winsc
    print('you win')
    winsc=+1
    scorecount()
def tie():
    print('its a tie')
    scorecount()
def lose():
    global losesc
    print('you lose')
    losesc=+1
    scorecount()
while go==True:
    player=input("rock, paper, scissors, shoot!")
    computer=random.choice(rps)
    print(computer, 'vs', player)
    if computer=='rock':
        if player=='rock':
            tie()
        elif player=='paper':
            win()
        elif player== 'scissors':
            lose()
    elif computer=='paper':
        if player=='paper':
            tie()
        elif player=='scissors':
            win()
        elif player== 'rock':
            lose()
    elif computer=='scissors':
        if player=='scissors':
            tie()
        elif player=='paper':
            win()
        elif player== 'rock':
            lose()
    else:
        print('invalid answer')
    go_on=input('continue? y/n')
    if go_on=='y':
        go=True
    else:
        go=False