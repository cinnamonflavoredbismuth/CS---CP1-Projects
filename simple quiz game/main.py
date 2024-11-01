#Cecily Strong ProficiencyTest: Simple Quiz Game
#HEHEHHEHEHEHE PREPARE TO GET QUIZZED ON BATMAN LORE
correct=0
questions=0
right=0
def q1():
    global correct
    global questions
    global right
    'if this is wrong go to ezq2'
    'if right go to q2'
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
    if answer==('tbd'):
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
          C:
          D:""")
    if answer==('tbd'):
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
    if answer==('tbd'):
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
    if answer==('tbd'):
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
    if answer==('tbd'):
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
    if answer==('tbd'):
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
    if answer==('tbd'):
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
    if answer==('tbd'):
        print('you got it right!')
        correct +=1
        right=True
    else:
        print('you got it wrong')
        right=False