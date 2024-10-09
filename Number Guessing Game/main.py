#Cecily Strong RAID: Number Guessing Game
import random
number= random.randint(1,10)
userNum=0
while userNum!=number:
    userNum=int(input("what is my number?"))
    if userNum>number:
        print("too high!")
    else:
        print("too low!")
else:
    print("congradulations! You got it right!")