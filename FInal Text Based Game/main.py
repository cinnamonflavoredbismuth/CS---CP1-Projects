#Cecily Strong FINAL: Implementation
import random

#player stuff

health=0
xp=0
speed=0
inventory=[]

#options for menus

mainMenu=['1. Naviation','2. Inventory','3. Stats']
stats=[health, xp, speed, inventory]
inventoryOptions=['1.Equip','2.Eat','3.Drop','4.Back']
fightOptions=['1. Attack','2.Item','3. Run away']
itemOptions=['1.Pick up','2.Ignore']
room=0
monster=0
Item=0
Weapon=0
roomItem=[]
moveNav=[]

#rooms

def firstRoom():
    global room
    global monster
    global roomItem
    global moveNav
    room='first room'
    firstRoomItem=['Baseball Bat']
    roomItem=firstRoomItem
    moveNav=['Left Room', 'Right Room']
def leftRoom():
    global room
    global monster
    global roomItem
    global moveNav
    room='Left room'
    monster=['beginning monster']
    leftItem=['Health Potion']
    roomItem=leftItem
    moveNav=['Courtyard', 'Dining Room','First Room']
def rightRoom():

    global room
    global monster
    global roomItem
    room='Right room'
    monster=['beginning monster']
    rightItem=['Health Potion']
    roomItem=rightItem
    global moveNav
    moveNav=['Kitchen', 'Bathroom','Dining Room']
def courtyard():
    global room
    global monster
    global roomItem
    room='Right room'
    monster=['beginning monster']
    rightItem=['Health Potion']
    roomItem=rightItem
    global moveNav
    moveNav=['Kitchen', 'Bathroom','Dining Room']
