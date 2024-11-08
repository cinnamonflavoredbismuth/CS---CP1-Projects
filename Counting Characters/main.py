#Cecily Strong SkillPractice: Counting characters
a=0
b=0
c=0
d=0
e=0
grid=[
['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A']  
]
for i in range(len(grid)):
    for x in range(len(grid)):
        if grid[i][x]=='A':
            a+=1
        elif grid[i][x]=='B':
            b+=1
        elif grid[i][x]=='C':
            c+=1
        elif grid[i][x]=='D':
            d+=1
        elif grid[i][x]=='E':
            e+=1
print("A:",a)
print("B:",b)
print("C:",c)
print("D:",d)
print("E:",e)