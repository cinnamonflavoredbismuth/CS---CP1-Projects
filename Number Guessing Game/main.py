#Cecily Strong RAID: Number Guessing Game
import random
play='yes'
while play=='yes':
    number= random.randint(1,10)
    userNum=0
    while userNum!=number:
        #thSese are the instructions
        userNum=int(input("I picked a number between 1 and 10, what is my number?"))
        if userNum>number:
            print("too high!")
        else:
            if userNum<number:
                print("too low!")
    else:
        print("congradulations! You got it right!")
        playagain=input("play again? Y/N")
        if playagain==('Y' or 'y'or'yes'):
            play='yes'
        else:
            play='no' #required so the code doesn't run forever
print("thank you for playing")