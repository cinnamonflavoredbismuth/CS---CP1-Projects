#Cecily Strong SkillPractice: Password Validator
passwordbad=True
password=''
'''
while passwordbad==True:
    password=input("type your password")
    if (not ('0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9')in password) or len(password)<8 or (not('!'or'@'or'$'or'%'or'^'or'&'or'*')in password):
        if (not ('0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9')in password):
            print('add a number')
        if len(password)<8:
            print('make it longer')
        if (not('!'or'@'or'$'or'%'or'^'or'&'or'*' or')'or'('or'#')in password):
            print("add a special character")
    else:
        print("you have created a strong password!")
        passwordbad=False
'''
password='c@t0'
print("is there a special character?")
if (not('@'or'^') in password):
    print(False)
else:
    print(True)