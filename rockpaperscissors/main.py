#Cecily Strong ProficiencyTest: Rock, Paper, Scissors
'''for x in range (12):
    for n in range(0,13*y,y):
        underline = "\033[4m" 
        reset = "\033[0m"
        print(f"{underline}",n,end='|')
    print('')
    y+=1'''

#winning_numbers=[winningvarsA,]
y=0
for x in range (3):
    for n in range(0,3):
        underline = "\033[4m" 
        reset = "\033[0m"
        print(f"|{underline}",' ',end='|')
    print('')
    y+=1