ogword=input("type your word")
listogword=list(ogword)
listogword.append(ogword[0])
listogword.pop(0)

print("".join(listogword)+"ay")