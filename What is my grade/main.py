#Cecily Strong SkillPractice: What is My Grade
grades=[]
def gradecheck():
    if percent>=93:
        grade="you have an A"
    elif percent>=90:
        grade="you have an A-"
    elif percent>=87.1:
        grade="you have a B+"
    elif percent>=83:
        grade="you have a B"
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
while start=='yes':  
    classname=input("which class is this for?")
    classes.append(classname)
   # print(classes)
    percent=int(input("what is your percentage"))
    gradecheck()
  #  print(grades)
    start=input("another class? yes/no")
    if start==('yes'):
        start='yes'
    else:
        start='no'
else:
    a=0
    while a<len(grades):
        print(str(grades[a]), "in", str(classes[a]))
        a+=1
print("thank you")