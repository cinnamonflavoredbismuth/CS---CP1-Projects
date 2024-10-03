#Cecily Strong ProficiencyTest: Shopping list manager
#def remove():
#        remove=input("what would you like to remove?")
#        shoppinglist.remove(remove)
#       print(shoppinglist)
#def add():
#        add=input("what would you like to add?")
#        shoppinglist.append(add)
#        print(shoppinglist)
shoppinglist=[0]

#action=0
#hile action is 3:
action = input("""What would you like to do?
                          Enter 1 to add item
                          Enter 2 to remove item
                          Enter 3 to leave the list:\n""")
if action =="1":
    remove=input("what would you like to remove?")
    shoppinglist.remove(remove)
    print(shoppinglist)
elif action =="2":
    remove=input("what would you like to remove?")
    shoppinglist.remove(remove)
    print(shoppinglist)
else:
    print
    print("Have a nice day!")