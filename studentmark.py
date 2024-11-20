#!/usr/bin/python3
student={}
while True:
    name=input("Enter the name of the student: and quit for exiting \t")
    if name.lower() == 'quit':
        break
    marks=[]
    subjects=['English', 'Maths', 'Physics', 'Biology', 'History']
    for i in subjects:
        mark=int(input(f"Enter the mark of {i} is: \t"))
        marks.append(mark)
    student[name]=marks
print(student)
for name in student.keys():
    total=0
    qualified='Pass'
    for mark in student[name]:
        total += mark
    if total < 250:
        qualified = 'Fail'
    print(f"{name:<8} Total mark {total:3} {qualified}")


