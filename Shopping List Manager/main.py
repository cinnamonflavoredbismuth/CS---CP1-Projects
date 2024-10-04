#Cecily Strong ProficiencyTest: Shopping list manager

shoppinglist=[]
s=0
while True:
    action = input("""What would you like to do?
                   
                          Enter 1 to add item
                   
                          Enter 2 to remove item
                   
                          Enter 3 to leave the list:\n""")
    if action =="1":
        add=input("what would you like to add?")
        shoppinglist.append(add)
        print(shoppinglist)


 
    elif action =="2":
        remove=input("what would you like to remove?")
        shoppinglist.remove(remove)
        print(shoppinglist)
        

    else:
        print("Have a nice day!")
        break