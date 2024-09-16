#Cecily Strong Raid fibbonaci sequence
numDoublePrevious=0
currentNumPrevious=1
currentNum=currentNumPrevious+numDoublePrevious
while currentNum < 10000000:
    currentNum=currentNumPrevious+numDoublePrevious
    str(currentNum)
    print(currentNum, end=" ")
    int(currentNum)
    numDoublePrevious=currentNumPrevious
    currentNumPrevious=currentNum