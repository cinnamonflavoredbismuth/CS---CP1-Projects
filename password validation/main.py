#Cecily Strong SkillPractice: Password Validator
passwordbad=0
password=''
#'''
while passwordbad<3:
    passwordbad=0
    password=input("type your password")
    if '0' in password or'1' in password or'2' in password or'3' in password or'4' in password or'5' in password or'6' in password or'7' in password or'8' in password or'9' in password :
            passwordbad+=1
    else:
            print('add a number')
    if len(password)>=8:
            passwordbad+=1
    else:
            print('make it longer')
    if '!' in password or '@' in password or '^' in password or'$' in password or'%' in password or'^' in password or'&' in password or'*' in password or')' in password or'(' in password or'#' in password:
            passwordbad+=1
    else:
            print("add a special character")

print('password authorized')