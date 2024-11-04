#Cecily Strong ProficiencyTest: Simple Quiz Game
#HEHEHHEHEHEHE PREPARE TO GET QUIZZED ON BATMAN LORE
correct=0
questions=0
right=0
def q1():
    global correct
    global questions
    global right
    print('q1')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
    if answer==('B'):
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
    print('')
    answer=input("""A:
B:
C:
D:""")
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
                ezq3()
                if right==True:
                    q4()
                else:
                    ezq4()
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