#Cecily Strong ProficiencyTest: Secret Cypher
changeby=int(input("How many do you want the cipher to shift by?"))
words=input("type your cipher")
wordslist=list(words)

s=0
while s < len(wordslist):
        wordslist[s]=ord(wordslist[s])
        wordslist[s]+=changeby
        wordslist[s]=chr(wordslist[s])
        s+=1

print("".join(wordslist))