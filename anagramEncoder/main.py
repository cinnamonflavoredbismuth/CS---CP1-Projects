input=input("type your name")
name=[x for x in input]
import random
random.shuffle(name)
name2=' '.join(name)
print(name2)