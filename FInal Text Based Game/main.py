#Cecily Strong FINAL: Implementation
import random

#note to self: variables are camelCase while functions are snake_case

#player stuff
#done

def varSetup():
    global inventory,mainMenu,stats,inventoryOptions,fightOptions,itemOptions,roomItem,monsters,navigation,room,monster,item,weapon,moveNav,choice,monHealth,fightChoose,suceed,whatDo,weapons,weaponStats,foods
    global xp,speed,totalHealth,rooms,health,yesNo,itemsOrMonsters
    xp=0
    totalHealth=5
    health=totalHealth
    speed=1
    inventory=[0]

    #options for menus
    #done

    mainMenu=['Menu','Naviation','Inventory','Stats','Room Options']
    stats={'health':health,'XP':xp,'Speed':speed}
    inventoryOptions=['Menu','Equip','Eat','Drop','Back']
    fightOptions=[0,'Attack','Item','Run away']
    itemOptions=['Menu','Pick up','Ignore']
    itemsOrMonsters=['Menu','Items in room','Monsters in room']
    yesNo=['Menu','Yes','No']
    rooms = [0,'First room','Left room','Right room','Courtyard','Dining room',
         'kitchen','Bathroom','Fence','Orchard','Foyer','Secret passage',
         'Garden','Well','Fence','Backdoor',
         'Hallway','Window','Master Bedroom']
    #options for all the rooms
    #key for me so I can remember what index every room is
    ['1. First room','2. Left room','3. Right room','4. Courtyard','5.Dining room',
         '6. kitchen','7. Bathroom','8. Fence','9. Orchard','10. Foyer','11. Secret passage',
         '12.Garden','13. Well','14. Fence2','15. Backdoor',
         '16. Hallway','17. Window','18. Master Bedroom']

    #items in rooms
    #done
    roomItem=[0,['Menu','Baseball Bat'],['Menu','Hp recovery potion'],['Menu','Hp recovery potion'],
          ['Menu','Hp recovery potion'],['Menu','Knife'],[0],[0],[0],[0],[0],['Menu','Strawberries','Key'],
          ['Menu','Key'],[0],['Menu','Rusty Bell'],[0],[0],[0],[0]]

    #monsters in rooms 
    #done
    monsters=[0,[0],[0,'Beginning Monster'],[0,'Beginning Monster'],[0,'Ghost'],[0,'Hangry Person'],
          [0,'Angry Cook'],[0,'Soap'],[0,'Electric Fence'],[0,'Apple'],[0,'Ghost'],
          [0],[0],[0,'Water'],[0,'Electric Fence'],[0],[0,'Ghost'],[0],
          [0,'Final Boss']]

    #navigation
    #done
    navigation=[0,['Menu',rooms[2],rooms[3]],['Menu',rooms[4],rooms[5],rooms[1]] ,['Menu',rooms[6],rooms[7],rooms[1]],
            ['Menu',rooms[8],rooms[9],rooms[2]],['Menu',rooms[10],rooms[11],rooms[2]],['Menu',rooms[11],rooms[3]],
            ['Menu',rooms[13],rooms[3]],['Menu',rooms[4],rooms[15]],['Menu',rooms[15],rooms[4]],
            ['Menu',rooms[15],rooms[16],rooms[5]],['Menu',rooms[18],rooms[5],rooms[6],rooms[12],rooms[16]],
            ['Menu',rooms[11],rooms[13]],['Menu',rooms[12],rooms[14],rooms[7]],['Menu',rooms[17],rooms[13]],
            ['Menu',rooms[8],rooms[9],rooms[10],rooms[16]],['Menu',rooms[15],rooms[10],rooms[11],rooms[18]],
            ['Menu',rooms[18],rooms[14]],['Menu',rooms[16],rooms[11],rooms[17]]]

    #variable setup
    room=0 #current room
    monster=0 #current monster in room
    item=0 #current item
    weapon=1 #current weapon
    moveNav=0 #navigation choice
    choice=0 #movement choice. Note: try to make all choice variables same variable
    monTotal=5
    monHealth=monTotal
    room=1
    fightChoose=0
    suceed=0
    whatDo=0
    weapons=['Baseball Bat','Knife']
    weaponStats=[2,3]
    foods=['Hp recovery potion','Strawberries']
#print list
def list_print(x):
    for item in x:
        print(f"{x.index(item)}. {item}")
        
#inventory
def inventory_options():
    global choice,inventory,whatDo,health,totalHealth,weapon,item
    exit=False
    while exit!=True:
        print('What item do you want to select?')
        list_print(inventory)
        choice=int(input())
        if choice!=0:
            print(f"you selected the {inventory[choice]}! press which number you would like to do with it")
            list_print(inventoryOptions)
            whatDo=int(input())
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
        else:
            main_menu()   
#main menu
def main_menu():
    global mainMenu,rooms,room,navigation,moveNav,inventory,stats,choice,exit,oldRoom
    exit=False
    print('you are in the',rooms[room])
    list_print(mainMenu)
    choice=int(input())
    if choice==1: #Navigation Options
        oldRoom=room
        print('type which number of room you want to go')
        list_print(navigation[room])
        choice=int(input())
        if choice!=0 and choice<=len(navigation[room]):
            room=navigation[room][choice]
            room=rooms.index(room)
            if room==11:
                number=int(input('what is the password?'))
                if number==1324 or 'a paper that says 1324' in inventory:
                    pass
                else:
                    print('Wrong password')
                    room=oldRoom
                    main_menu()
            if room==18:
                if 'Key'in inventory:
                    pass
                else:
                    print("It's locked...")
                    room=oldRoom
                    main_menu()
            new_room()            
        else:
            print('Exit')
            main_menu()
    elif choice==2:#inventory
        inventory_options()
    elif choice==3:#Stats
        print(stats)
        main_menu()
    elif choice==4:
        print('What would you like to do?')
        list_print(itemsOrMonsters)
        choice=int(input())
        if choice==1:
            print("Items:")
            if roomItem[room]!=0:
                list_print(roomItem[room])
                print("Do you want to interact with this item?")
                print(yesNo)
                choice=int(input())
                if choice==1:
                    room_item()
                    main_menu()
                else:
                    main_menu()
            else:
                print('No Items')
        elif choice==2:
            print('Monsters:')
            if monsters[room]!=0:
                list_print(monsters[room])
                print("Do you want to fight this monster?")
                print(yesNo)
                choice=int(input())
                if choice==1:
                    fight_function()
                    main_menu()
                else:
                    main_menu()
            else:
                print('No monsters')
        else:
            main_menu()
    else:
        print("Why... would you do that?")
        main_menu()
#fight mechanics
def fight_function():
    #beginning stuff. declare monsters and allat
    global monsters,room,health,xp,monTotal,monHealth,fightChoose,suceed,speed,choice,monWeapon,monsterDrop
    global totalHealth,escape
    escape=False
    if room==(2 or 3)and len(monsters[room])>1:#beginning monster
        monTotal=5
        monWeapon=1
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
    while monHealth>0:
        #Beginning script. Health of both players, ect
        if 'Rusty Bell' in inventory and room==(4 or 10 or 16)and len(monsters[room])>1:
            print('You scared the ghost away! would you like to fight it anyway?')
            list_print(yesNo)
            choice=int(input())
            if choice==1:
                pass
            else:
               break
        print(f'Your health is: {health}/{totalHealth}')
        print(f"The {monsters[room][-1]}'s health is: {monHealth}/{monTotal}")
        print('what would you like to do?')
        list_print(fightOptions)
        fightChoose=int(input())
        #Player's Turn
        playerTurn=True
        while playerTurn==True:
            if fightChoose==1:#attack
                suceed=random.randint(0,14)
                #print(suceed)
                if suceed<=xp:
                    print('Success! your attack landed!')
                    monHealth=-weapon
                else:
                    print('You missed')
            
            elif fightChoose==2:#Item
                inventory_options()
            elif fightChoose==3:#run away
                suceed=random.randint(0,14)
                #print(suceed)
                if suceed<=speed:
                    print('You successfully escaped')
                    speed+=1
                    escape=True
                    break
                    
                else:
                    print("You couldn't run away")
            else:
                print("invalid choice")
            input()
            playerTurn=False
        #monsters turn
        if escape==True:
            break
        else:
            suceed=random.randint(0,14)
            #print(suceed)
            if suceed<5:
                print('The monster hit you!')
                health-=monWeapon
            else:
                print("The monster missed") 
    else:
        monsters[room].pop(1)
        print('You win!')
        monsterDrop=random.randint(0,10)
        if monsterDrop==1:
            roomItem[room].append('Rusty Bell')
        if monsterDrop==2:
            roomItem[room].append('a paper that says 1324')
        if monsterDrop==3:
            roomItem[room].append('Key')
        xp+=1
        totalHealth+=1
        health=totalHealth       
#items in room mechanics
#done
def room_item():
    global roomItem,room,itemSelect,choice,itemOptions,inventory
    print('press the number of the item you want to select')
    list_print(roomItem[room])
    itemSelect=int(input())
    if itemSelect>0:
        print(roomItem[room][itemSelect])
        list_print(itemOptions)
        choice=int(input())
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
        if len(roomItem[room])>1:
            room_item()
        else:
            main_menu()
    else:
        if len(roomItem[room])>1:
            room_item()
        else:
            main_menu()
#Reset function
def in_the_beninging():
    varSetup()
    print('you are stuck in a haunted house! You have to escape')
    new_room()
    while health>0:
        pass
    else:
        print("You died! would you like to continue?")
        list_print(yesNo)
        dead=int(input())
        if dead==1:
            in_the_beninging()
        else:
            print('thanks for playing')
in_the_beninging()