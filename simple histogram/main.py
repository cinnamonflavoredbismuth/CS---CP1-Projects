#Cecily Strong RAID: Simple Histogram
numbers=input("type a list of 6 numbers")
histogram=numbers.split()
print(histogram)
i=0

for i in range(len(histogram)):
    xlist=[]
    for x in range(int(histogram[i])):
        xlist.append('x')
    printx=''.join(xlist)
    print(f"{i+1}:{printx}",end='')
    print()