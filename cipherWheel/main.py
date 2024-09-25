#Cecily Strong ProficiencyTest: Secret Cypher
#I'm going to use this for the book im reading :)
#yourText=input(
num=int(input("press 1 for Caesar Cipher, press 2 for atbash cipher, press 3 to translate a ceasar cipher to english"))
if num==1:
    plainText=input("type your cipher")
    textList=[x for x in plainText]
    print(textList)
    i=0
    for i, element in enumerate(textList):
        oglet=ord[i]
        shiftlet=oglet+4
        chr(shiftlet)
    i+=1

if num==2:
    plainText=input("type your cipher")
    textList=[x for x in plainText]
    print(textList)
    i=0
    while i < len(textList):
        def replace (str,num):
           if textList[i]==str:
              textList[i]=num
        replace('a','z')
        replace('b','y')
        replace('c','x')
        replace('d','w')
        replace('e','v')
        replace('f','u')
        replace('g','t')
        replace('h','s')
        replace('i','r')
        replace('j','q')
        replace('k','p')
        replace('l','o')
        replace('m','n')
        replace('n','m')
        replace('o','l')
        replace('p','k')
        replace('q','j')
        replace('r','i')
        replace('s','h')
        replace('t','g')
        replace('u','f')
        replace('v','e')
        replace('w','d')
        replace('x','c')
        replace('y','b')
        replace('z','a')
        i += 1

textList.join(textList)
print(textList)