#Cecily Strong RAID: Countdown Timer
import time
seconds=int(input("how many seconds long do you want the timer?"))
while seconds>=0:
    print(seconds)
    time.sleep(1)
    seconds-=1
print("beep! your timer is done")