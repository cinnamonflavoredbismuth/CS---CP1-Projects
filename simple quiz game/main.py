#Cecily Strong ProficiencyTest: Simple Quiz Game
#HEHEHHEHEHEHE PREPARE TO GET QUIZZED ON BATMAN STUFF
correct=0
questions=0
right=0
play=True
def q1():
    global correct
    global questions
    global right
    print('Who was the second Robin?')
    answer=input("""A:Jason Todd
B:Robin
C:Damian Wayne
D:Tim Drake""")
    if answer==('A'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
    questions+=1
def q2():
    global correct
    global questions
    global right
    'if this is wrong go to ezq2'
    'if right go to q3'
    print('How many Robins have there been?')
    answer=input("""A:3
B:4
C:1
D:5""")
    if answer==('D'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def q3():
    global correct
    global questions
    global right
    'if this is wrong go to ezq2'
    'if right go to q4'
    print('How many children does Bruce Wayne have?')
    answer=input("""A:4
B:7
C:8
D:1""")
    if answer==('C'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def q4():
    global correct
    global questions
    global right
    'if this is wrong go to ezq2'
    'if right go to q5'
    print('What hero is Duke Thomas?')
    answer=input("""A:Signal
B:Robin
C:Black Bat
D:Nightwing""")
    if answer==('A'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def q5():
    global correct
    global questions
    global right
    'if this is wrong then it sucks to suck'
    'if right then wow youre a nerd'
    print("Who is Batman's one true love?")
    answer=input("""A:Catwoman
B:Justice
C:Talia al ghul
D:The Joker""")
    if answer==('B'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def ezq2():
    global correct
    global questions
    global right
    'if this is wrong go to ezq3'
    'if right go to q2'
    print("Who is Batman's most famous enemy?")
    answer=input("""A:The Riddler
B:The Penguin
C:Superman
D:The Joker""")
    if answer==('D'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def ezq3():
    global correct
    global questions
    global right
    'if this is wrong go to ezq4'
    'if right go to q2'
    print('What city does Batman protect?')
    answer=input("""A:New York
B:Gotham
C:Manhattan
D:Metropolis""")
    if answer==('D'):
        print('you got it right!')
        right=True
        correct +=1
    else:
        print('you got it wrong')
        right=False
def ezq4():
    global correct
    global questions
    global right
    'if this is wrong go to ezq5'
    'if right go to q2'
    print('What is the car Batman drives called?')
    answer=input("""A:The Batmobile
B:The Bat-Car
C:The Car
D:Batman needs a car?""")
    if answer==('A'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
def ezq5():
    global correct
    global right
    global questions
    print("What is Batman's secret identity?")
    answer=input("""A:Dracula
B:Oswald Cobblepot
C:Bruce Wayne
D:Tony Stark""")
    if answer==('C'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False
while play==True:
    play=True
    print('welcome to the batman trivia quiz! where you prove if you are a freaking nerd')
    q1()#1
    if right==True:
        q2()#2
        if right==True:
            q3()#3
            if right==True:
                q4()#4
                if right==True:
                    q5()#5
                    play=False
                else:
                    ezq2()#5
                    play=False
            else:
                ezq2()#4
                if right==True:
                    q4()#5
                    play=False
                else:
                    ezq3()#5
                    play=False
        else:
            ezq2()#3
            if right==True:
                q3()#4
                if right==True:
                    q4()#5
                    play=False
                else:
                    ezq2()#5
                    play=False
            else:
                ezq3()#4
                if right==True:
                    q3()#5
                    play=False
                else:
                    ezq4()#5
                    play=False
    else:
        ezq2()#2
        if right==True:
            q2()#3
            if right==True:
                q3()#4
                if right==True:
                    q4()#5
                    play=False
                else:
                    ezq3()#5
                    play=False
            else:
                ezq3()#4
                if right==True:
                    q4()#5
                    play=False
                else:
                    ezq4()#5
                    play=False
        else:
            ezq3()#3
            if right==True:
                q2()#4
                if right==True:
                    q3()#5
                    play=False
                else:
                    ezq4()#5
                    play=False
            else:
                ezq4()#4
                if right==True:
                    q2()#5
                    play=False
                else:
                    ezq5()#5
                    play=False
else:
    print('you got',correct,'out of 5 questions correct!')
