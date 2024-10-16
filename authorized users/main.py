#Cecily Strong ProficiencyTest: Authorized
authorized=['Cecily','Edward','Jonathan','Jack','Oswald','Harvey', 'Pamela', "Waylon"]
admin=['Cecily']
name=input("what is your name?")
if name in authorized:
    if name in admin:
        print("You are an administrator")
    else:
        print("You are authorized")
else:
    print("You are not authorized")