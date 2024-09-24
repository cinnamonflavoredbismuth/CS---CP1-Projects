#Cecily Strong ProficiencyTest: Secret Cypher
#I'm going to use this for the book im reading :)
#yourText=input(
print("Caesar Cipher")
plainText=input("type your cipher")
textList=[x for x in plainText]
print(textList)
i=0
while i < len(textList):
    def replace (str,num):
       if textList[i]==str:
          textList[i]=num
    replace('a','d')
    replace('b','e')
    replace('c','f')
    replace('d','g')
    replace('e','h')
    replace('f','i')
    replace('g','j')
    replace('h','k')
    replace('i','l')
    replace('j','m')
    replace('k','n')
    replace('l','o')
    replace('m','p')
    replace('n','q')
    replace('o','r')
    replace('p','s')
    replace('q','t')
    replace('r','u')
    replace('s','v')
    replace('t','w')
    replace('u','y')
    replace('v','z')
    replace('w','a')
    replace('x','b')
    replace('y','c')
    replace('z','d')
    i += 1

textList.join(textList)
print(textList)