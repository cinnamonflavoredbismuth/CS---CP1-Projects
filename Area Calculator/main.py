#Cecily Strong Area Calculator
again="Y"
if again ="Y":
    begin=int(input("press 1 for square, 2 for rectangle, 3 for triangle, 4 for circle, 5 for trapazoid"))

    if begin==1:
        num1=int(input("type your number"))
        product=num1**2
    if begin==2:
        num1=int(input("type your number"))
        num2=int(input("second number"))
        product=num1*num2
    if begin==3:
        num1=int(input("type your number"))
        num2=int(input("second number"))
        product=(num1*num2)/2
    if begin==4:
        num1=int(input("type your number"))
        product=3.14*(num1**2)
    if begin==5:
        num1=int(input("type your base"))
        num2=int(input("second base"))
        num3=int(input("type your height"))
        product=((num1+num2)/2)*num3
    print("your answer is:",product)
    again=input("do you want to go again? Y/N")