#Cecily Strong ProficiencyTest: Rock, Paper, Scissors
import random
a1=' '
a1input='top left'
a2=' '
a2input='top middle'
a3=' '
a3input='top right'
b1=' '
b1input='middle left'
b2=' '
b2input='middle'
b3=' '
b3input='middle right'
c1=' '
c1input='bottom left'
c2=' '
c2input='bottom middle'
c3=' '
c3input='right middle'
winA=[a1,a2,a3]
winB=[b1,b2,b3]
winC=[c1,c2,c3]
win1=[a1,b1,c1]
win2=[a2,b2,c2]
win3=[a3,b3,c3]
winac1=[a1,b2,c3]
winac2=[a3,b2,b1]
winningnumbers=[winA,winB,winC,win1,win2,win3,winac1,winac2]
coordinatesinput=[a1input,a2input,a3input,b1input,b2input,b3input,c1input,c2input,c3input]
coordinates=[a1,a2,a3,b1,b2,b3,c1,c2,c3]
y=0
def board():
    def printboard(x1,x2,x3):
        def printrow(variable):
            underline = "\033[4m" 
            print(f"|{underline}",(variable),end='|')
        printrow(x1)
        printrow(x2)
        printrow(x3)
        print(' ')
    printboard(a1,a2,a3)
    printboard(b1,b2,b3)
    printboard(c1,c2,c3)
def Xturn():
    print("which square would you like?")
    X=input(', '.join(coordinatesinput))
    def lazyinput(coordinput, coord):
        if X==coordinput and coord== ' ':
            coord='X'
    lazyinput(coordinatesinput[1:],coordinates[1:])
    print()

Xturn()