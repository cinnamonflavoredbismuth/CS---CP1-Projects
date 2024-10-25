#Cecily Strong SkillPractice: Password Validator
passwordbad=True
while passwordbad==True:
    password=input("type your password")
    if (('0'or'1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9') not in password):
        print('you have a number')
    if len(password)<8:
        print('make it longer')
    if not'!'or'@'or'$'or'%'or'^'or'&'or'*'in password:
        print("add a special character")
    else:
        print("you have created a strong password!")
        passwordbad=False