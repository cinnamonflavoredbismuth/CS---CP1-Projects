#Cecily Strong ProficiencyTest: Multiplication Table
#backup
#number=int(input("what number would you like to multiply?"))
#for n in range(0,number*13,number):
#    print(str(n, end=' '))
y=1
x=0

for x in range (12):
    for n in range(0,13*y,y):
        underline = "\033[4m" 
        reset = "\033[0m"
        print(f"{underline}",n,"{underline}"end='|')
    print('')
    y+=1

