#Cecily Strong RAID: Character Creator
print("you wake up with amnesia...")
print("quick! you need to remember who you are!")
name=input("what is your name?")
race=input("""What is your race?
                Elf
                Dwarf
                Human
                Dragonborn
                Sigma""")
classs=input("""what is your class?
                Thief
                Fighter
                Wizard
                Archer
                Rizzler""")
hp=0
str=0
dex=0
int=0
invalidClass=False
invalidRace=False
secret=False
if race=='Elf':
    hp+=7
    str+=3
    dex+=7
    int+=10
elif race=='Dwarf':
    hp+=10
    str+=9
    dex+=3
    int+=3
elif race=='Human':
    hp+=5
    str+=5
    dex+=5
    int+=5
elif race=='Dragonborn':
    hp+=10
    str+=8
    dex+=5
    int+=4
elif race=='Sigma':
    hp+=0
    str+=0
    dex+=0
    int+=0
else:
    invalidRace=True
if classs=='Thief':
    hp+=4
    str+=4
    dex+=8
    int+=8
elif classs=='Fighter':
    hp+=10
    str+=8
    dex+=4
    int+=2
elif classs=='Wizard':
    hp+=2
    str+=2
    dex+=5
    int+=10
elif classs=='Archer':
    hp+=5
    str+=4
    dex+=8
    int+=8
elif classs=='Rizzler':
    hp+=0
    str+=0
    dex+=0
    int+=0
else:
    invalidClass=True
if race=='Sigma'and classs=='Rizzler':
    secret=True
    hp=99
    str=99
    dex=99
    int=99
if invalidClass==False and invalidRace==False:
    final=("""Your stats are...
          health [{}]
          strength [{}]
          dexterity [{}]
          intelligence [{}]""")
    print(final.format(hp,str,dex,int))
    if secret==True:
        print("you are the most sigma skibidi rizzler in the land")
else:
    if invalidClass==True:
        print("your class was invalid.")
    if invalidRace==True:
        print('your race is invalid.')
    if invalidClass==True and invalidRace==True:
        print("I'm impressed, the only thing that was valid was your name! try again.")