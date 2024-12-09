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

mainMenu=[0,'1. Naviation','2. Inventory','3. Stats']
stats=[health, xp, speed, inventory]
inventoryOptions=[0,'1.Equip','2.Eat','3.Drop','4.Back']
fightOptions=[0,'1. Attack','2.Item','3. Run away']
itemOptions=[0,'1.Pick up','2.Ignore']
rooms = [0,'First room','Left room','Right room','Courtyard','Dining room',
         'kitchen','Bathroom','Fence','Orchard','Foyer','Secret passage',
         'Garden','Well','Fence2','Backdoor',
         'Hallway','Window','Master Bedroom']
#options for all the rooms
#key for me so I can remember what index every room is
['1. First room','2. Left room','3. Right room','4. Courtyard','5.Dining room',
         '6. kitchen','7. Bathroom','8. Fence','9. Orchard','10. Foyer','11. Secret passage',
         '12.Garden','13. Well','14. Fence2','15. Backdoor',
         '16. Hallway','17. Window','18. Master Bedroom']

#items in rooms
#done

itemRoom1=[0,'Baseball Bat']
itemRoom2=[0,'Hp recovery potion'] 
itemRoom3=[0,'Hp recovery potion']
itemRoom4=[0,'Hp recovery potion']
itemRoom5=[0,'Knife']
itemRoom6=[0]
itemRoom7=[0]
itemRoom8=[0]
itemRoom9=[0]
itemRoom10=[0]
itemRoom11=[0,'Strawberries']
itemRoom12=[0,'Key']
itemRoom13=[0]
itemRoom14=[0,'Rusty Bell']
itemRoom15=[0]
itemRoom16=[0]
itemRoom17=[0]
itemRoom18=[0]
roomItem=[0,itemRoom1,itemRoom2,itemRoom3,itemRoom4,itemRoom5,itemRoom6,
          itemRoom7,itemRoom8,itemRoom9,itemRoom10,itemRoom11,itemRoom12,
          itemRoom13,itemRoom14,itemRoom15,itemRoom16,itemRoom17,itemRoom18]

#monsters in rooms 
#done

mon1=[0]
mon2=[0,'Beginning Monster'] 
mon3=[0,'Beginning Monster']
mon4=[0,'Ghost']
mon5=[0,'Hangry Person']
mon6=[0,'Angry Cook']
mon7=[0,'Soap']
mon8=[0,'Electric Fence']
mon9=[0,'Apple']
mon10=[0,'Ghost']
mon11=[0]
mon12=[0]
mon13=[0,'Water']
mon14=[0,'Electric Fence']
mon15=[0]
mon16=[0,'Ghost']
mon17=[0,'Owner of Estate']
mon18=[0,'Final Boss']
monsters=[0,mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,
          mon11,mon12,mon13,mon14,mon15,mon16,mon17,mon18]

#navigation
#done

nav1=[0,rooms[2],rooms[3]]
nav2=[0,rooms[4],rooms[5],rooms[1]] 
nav3=[0,rooms[6],rooms[7],rooms[1]]
nav4=[0,rooms[8],rooms[9],rooms[2]]
nav5=[0,rooms[10],rooms[11],rooms[2]]
nav6=[0,rooms[11],rooms[3]]
nav7=[0,rooms[13],rooms[3]]
nav8=[0,rooms[4],rooms[15]]
nav9=[0,rooms[15],rooms[4]]
nav10=[0,rooms[15],rooms[16],rooms[5]]
nav11=[0,rooms[18],rooms[5],rooms[6],rooms[12],rooms[16]]
nav12=[0,rooms[11],rooms[13]]
nav13=[0,rooms[12],rooms[14],rooms[7]]
nav14=[0,rooms[17],rooms[13]]
nav15=[0,rooms[8],rooms[9],rooms[10],rooms[16]]
nav16=[0,rooms[15],rooms[10],rooms[11],rooms[18]]
nav17=[0,rooms[18],rooms[14]]
nav18=[0,rooms[16],rooms[11],rooms[17]]
navigation=[0,nav1,nav2,nav3,nav4,nav5,nav6,nav7,nav8,nav9,nav10,
            nav11,nav12,nav13,nav14,nav15,nav16,nav17,nav18]

#variable setup
room=0 #current room
monster=0 #current monster in room
item=0 #current item
weapon=0 #current weapon
moveNav=0 

#rooms
room=1
print('you are in the',rooms[room])
print('type which number of room you want to go')
moveNav=input(navigation[room])
room=navigation[room][int(moveNav)]
room=room.index(room)
print('room=',room)
print(rooms[room])
