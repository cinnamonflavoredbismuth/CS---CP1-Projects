#Cecily Strong FINAL: Implementation
import random

#player stuff
#done

health=0
xp=0
speed=0
inventory=[]

#options for menus
#done

mainMenu=['1. Naviation','2. Inventory','3. Stats']
stats=[health, xp, speed, inventory]
inventoryOptions=['1.Equip','2.Eat','3.Drop','4.Back']
fightOptions=['1. Attack','2.Item','3. Run away']
itemOptions=['1.Pick up','2.Ignore']
rooms = [0,'1. First room','2. Left room','3. Right room','4. Courtyard','5.Dining room',
         '6. kitchen','7. Bathroom','8. Fence','9. Orchard','10. Foyer','11. Secret passage',
         '12.Garden','13. Well','14. Fence2','15. Backdoor',
         '16. Hallway','17. Window','18. Master Bedroom']

#items in rooms
#done

itemRoom1=['Baseball Bat']
itemRoom2=['Hp recovery potion'] 
itemRoom3=['Hp recovery potion']
itemRoom4=['Hp recovery potion']
itemRoom5=['Knife']
itemRoom6=[]
itemRoom7=[]
itemRoom8=[]
itemRoom9=[]
itemRoom10=[]
itemRoom11=['Strawberries']
itemRoom12=['Key']
itemRoom13=[]
itemRoom14=['Rusty Bell']
itemRoom15=[]
itemRoom16=[]
itemRoom17=[]
itemRoom18=[]
roomItem=[0,itemRoom1,itemRoom2,itemRoom3,itemRoom4,itemRoom5,itemRoom6,
          itemRoom7,itemRoom8,itemRoom9,itemRoom10,itemRoom11,itemRoom12,
          itemRoom13,itemRoom14,itemRoom15,itemRoom16,itemRoom17,itemRoom18]

#monsters in rooms 
#done

mon1=[]
mon2=['Beginning Monster'] 
mon3=['Beginning Monster']
mon4=['Ghost']
mon5=['Hangry Person']
mon6=['Angry Cook']
mon7=['Soap']
mon8=['Electric Fence']
mon9=['Apple']
mon10=['Ghost']
mon11=[]
mon12=[]
mon13=['Water']
mon14=['Electric Fence']
mon15=['']
mon16=['Ghost']
mon17=['Owner of Estate']
mon18=['Final Boss']
monsters=[0,mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,
          mon11,mon12,mon13,mon14,mon15,mon16,mon17,mon18]

#navigation

nav1=[rooms[1],rooms[2]]
nav2=[rooms[4],rooms[5],rooms[1]] 
nav3=[rooms[6],rooms[7],rooms[1]]
nav4=[rooms[8],rooms[9],rooms[2]]
nav5=[rooms[10],rooms[11],rooms[2]]
nav6=[rooms[11],rooms[3]]
nav7=[rooms[1],rooms[2]]
nav8=[rooms[1],rooms[2]]
nav9=[rooms[1],rooms[2]]
nav10=[rooms[1],rooms[2]]
nav11=[rooms[1],rooms[2]]
nav12=[rooms[1],rooms[2]]
nav13=[rooms[1],rooms[2]]
nav14=[rooms[1],rooms[2]]
nav15=[rooms[1],rooms[2]]
nav16=[rooms[1],rooms[2]]
nav17=[rooms[1],rooms[2]]
nav18=[rooms[1],rooms[2]]
navigation=[0,nav1,nav2,nav3,nav4,nav5,nav6,nav7,nav8,nav9,nav10,
            nav11,nav12,nav13,nav14,nav15,nav16,nav17],nav18

room=0
monster=0
Item=0
Weapon=0

moveNav=[]
movechoice=0

#rooms

room=1
if room==1:
    moveNav=['1. Left Room', '2. Right Room']
    if movechoice==1:
        room=2
    if movechoice==2:
        room=3
print(roomItem[room][1])
