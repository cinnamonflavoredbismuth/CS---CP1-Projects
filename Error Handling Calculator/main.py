#Cecily Strong SkillPractice: Error Handling Calculator
run=True
def main():
    operations=['+','-','*','/','**','//']
    try:
        number1=int(input('what is your first number?'))
    except:
        print("type an integer")
    try:
        number2=int(input('what is your second number?'))
    except:
        print("type an integer")

    print("what operation do you want to perform?")
    operation=input("+(addition),-(subtraction),*(multiplication),/(division),**(exponent),//(modular division)")
    if operation in operations:
        if operation=='+':
            print(number1+number2)
        if operation=='-':
            print(number1-number2)
        if operation=='*':
            print(number1*number2)
        if operation=='/':
            if number2==0:
                print("you silly goose, you can't divide by zero!")
            else:
                print(number1/number2)
        if operation=='**':
            print(number1**number2)
        if operation=='//':
            if number2==0:
                print("you silly goose, you can't divide by zero!")
                main()
            else:
                print(number1//number2)
while run==True:
    main()
    ask=input("again? y/n")
    if ask=='y':
        run=True
    else:
        run=False