#Cecily Strong ProficiencyTest: Graded Quiz
score = 0
print("math quiz! lets see if you know basic math")
question = int(input("2+3="))
if question == 5:
    score += 1
question = int(input("3*4="))
if question == 12:
    score += 1
question = int(input("64/4="))
if question == 16:
    score += 1
question = int(input("17-3="))
if question == 14:
    score += 1
question = int(input("4^2="))
if question == 8:
    score += 1

print("Congradulations! you got", score, "out of 5!")