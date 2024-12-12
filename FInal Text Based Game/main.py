#Cecily Strong FINAL: Implementation
import random

#note to self: variables are camelCase while functions are snake_case

#player stuff
#done


xp=0
totalHealth=5
health=totalHealth
speed=1
inventory=[0]

#options for menus
#done

mainMenu=[0,'1. Naviation','2. Inventory','3. Stats','4. Room Options']
stats={'health':health,'XP':xp,'Speed':speed}
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
weapon=1 #current weapon
moveNav=0 #navigation choice
choice=0 #movement choice. Note: try to make all choice variables same variable
monTotal=5
monHealth=monTotal
room=2
fightChoose=0
suceed=0
whatDo=0
weapons=['Baseball Bat','Knife']
weaponStats=[3,5]
foods=['Hp recovery potion','Strawberries']
#inventory
def inventory_options():
    global choice,inventory,whatDo,health,totalHealth,weapon,item
    exit=False
    while exit!=True:
        print('What item do you want to select? Press 0 to exit')
        choice=int(input(inventory))
        print(f"you selected the {inventory[choice]}! press which number you would like to do with it, and press 0 to exit")
        whatDo=int(input(inventoryOptions))
        if whatDo==1: #Equip
            if inventory[choice] in weapons:
                weapon=weaponStats[weapons.index(inventory[choice])]
            else:
                print('thats not a weapon')
        elif whatDo==2:#Eat
            if inventory[choice] in foods:
                print('yummy')
                health=totalHealth
                inventory.pop(choice)
            else:
                print("you can't eat that...")
        elif whatDo==3:#Drop
            roomItem[room].append(inventory[choice])
            inventory.pop(choice)
        elif whatDo==4:
            pass
        elif whatDo==0:
            break
        else:
            print('that is not a valid option')
        
#main menu
def main_menu():
    global mainMenu,rooms,room,navigation,moveNav,inventory,stats,choice
    exit=False

    print('you are in the',rooms[room])
    choice=int(input(mainMenu))
    if choice==1: #Navigation Options
        print('type which number of room you want to go, press 0 to exit')
        choice=int(input(navigation[room]))
        if choice!=0 and choice<=len(navigation[room]):
            if room==11:
                choice=int(input('what is the password?'))
                if choice==1324:
                    pass
                else:
                    print('Wrong password')
                    main_menu()
            room=navigation[room][moveNav]
            room=rooms.index(room)
            new_room()            
        else:
            print('Exit')
            main_menu()
    if choice==2:#inventory
        inventory_options()
    if choice==3:#Stats
        print(stats)
    if choice==4:
        print(roomItem[room])
        print(monsters[room])
#fight mechanics
def fight_function():
    #beginning stuff. declare monsters and allat
    global monsters,room,health,xp,monTotal,monHealth,fightChoose,suceed,speed,choice
    if room==(2 or 3)and len(monsters[room])>1:#beginning monster
        monTotal=5
    elif room==(4 or 10 or 16)and len(monsters[room])>1:#ghost 
            monTotal=16
    elif room==(5 or 6)and len(monsters[room])>1:#Cook and Hangry
        monTotal=7
    elif room==(7 or 9 or 13)and len(monsters[room])>1:#soap, apple, and water
        monTotal=13
    elif room==(8 or 14)and len(monsters[room])>1:#electric fence
        monTotal=12
    elif room==(17)and len(monsters[room])>1:#Owner (mini boss)
        monTotal=20
    elif room==(18)and len(monsters[room])>1:#Final Boss
        monTotal=30
    else:
        print('''There is no monster...
              did you break the code?''')
    monHealth=monTotal
    print(f'You encounter the {monsters[room][-1]}!')
    while monHealth>0 and health>0:
        #Beginning script. Health of both players, ect
        if 'Rusty Bell' in inventory and room==(4 or 10 or 16)and len(monsters[room])>1:
            print('You scared the ghost away! would you like to fight it anyway?')
            choice=int(input(""""1. Yes
                             2. No"""))
            if choice==1:
                pass
            else:
               break
        print(f'Your health is: {health}/{totalHealth}')
        print(f"The {monsters[room][-1]}'s health is: {monHealth}/{monTotal}")
        print('what would you like to do?')
        fightChoose=int(input(fightOptions))
        #Player's Turn
        if fightChoose==1:#attack
            suceed=random.randint(weapon+xp,14)
            print(suceed)
            if suceed<xp:
                print('Success! your attack landed!')
                monHealth=-1
            else:
                print('You missed')
        if fightChoose==2:#Item
            inventory_options()
        if fightChoose==3:
            suceed=random.randint(speed,14)
            print(suceed)
            if suceed<xp:
                print('You successfully escaped')
                speed+=1
                break
            else:
                print("You couldn't run away")
        
#items in room mechanics
#done
def room_item():
    global roomItem,room,itemSelect,choice,itemOptions,inventory
    print('press the number of the item you want to select, press 0 to exit')
    itemSelect=int(input(roomItem[room]))
    if itemSelect>0:
        print(roomItem[room][itemSelect])
        choice=int(input(itemOptions))
        if choice==1:
            inventory.append(roomItem[room][itemSelect])
            roomItem[room].pop(itemSelect)
            main_menu()
        else:
            main_menu()
    else:
        main_menu()
#new room function
#done
def new_room():
    global choice
    print('you are in the',rooms[room])
    if len(monsters[room])>1:
        fight_function()
    else:
        if len(roomItem[room])>1:
            room_item()
        else:
            main_menu()
new_room()