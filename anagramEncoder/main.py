import random
name=input("type your name")
list(name)

def scramble(name2):
    random.shuffle(name2)
    #name2=''.join(name)
    print(''.join(name2))
scramble(name)
scramble(name)
scramble(name)
scramble(name)
scramble(name)