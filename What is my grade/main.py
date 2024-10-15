#Cecily Strong SkillPractice: What is My Grade
#percent=[float(input("what is your grade percentage for period 1?")),
#         float(input("what is your grade percentage for period 2?")),
#         float(input("what is your grade percentage for period 3?")),
#         float(input("what is your grade percentage for period 6?")),
#         float(input("what is your grade percentage for period 7?")),
#         float(input("what is your grade percentage for period 8?")),]
grades=[]
def gradecheck():
    if percent>=93:
        grade="you have an A!"
    elif percent>=90:
        grade="you have an A-!"
    elif percent>=87.1:
        grade="you have a B+"
    elif percent>=83:
        grade="you have a B!"
    elif percent>=80:
        grade="you have a B-"
    elif percent>=77.1:
        grade="you have a C+"
    elif percent>=73:
        grade="you have a C"
    elif percent>=70:
        grade="you have a C-"
    elif percent>=67.1:
        grade="you have a D+"
    elif percent>=60:
        grade="you have a D"
    else:
        grade="you are failing"
    grades.append(grade)
start='yes'
classes=[]
if start=='yes':  
    classname=input("which class is this for?")
    classes.append(classname)
    percent=input("what is your percentage")
    gradecheck()
    start=input("another class? yes/no")
else:
    a>
    print
