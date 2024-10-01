#Cecily Strong ProficiencyTest: Secret Cypher
words=input("type your cipher")
wordslist=list(words)

for s in wordslist:
        wordslist.append(ord(s))
print(wordslist)