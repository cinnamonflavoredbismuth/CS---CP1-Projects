#Cecily Strong Proficency test: Simple calculator
print("use this calculator for 2 values")
print("what kind of math do you want?")
sign=input("type + for addition, - for subtraction, * for multiplication, / for dividion, ** for exponents, and // for rounded division")
number1=int(input("what is the first number in the equation?"))
number2=int(input("what is the second number in the equation?"))
if sign== "+":
    print("loading...")
    answer=(number1+number2)
if sign== "-":
    print("loading...")
    answer=(number1-number2)
if sign== "*":
    print("loading...")
    answer=(number1*number2) 
if sign== "/":
    print("loading...")
    answer=(number1/number2)  
if sign== "**":
    print("loading...")
    answer=(number1**number2)
if sign== "//":
    print("loading...")
    answer=(number1//number2)
print(answer)