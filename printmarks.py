#!/usr/bin/python3
marks=[]
subjects=['physics', 'maths', 'biology', 'history', 'zoology', 'history','botany', 'english']

for f in subjects:
    mark=int(input(f"Enter mark of {f} \n"))
    marks.append(mark)
for i in marks:
    if(i>50):
       print(f"mark is {i}and passed the eaxm, Congratulation!!")
    else:
        print(f"mark is {i} and Failed, Better luck next time")
total=0
for i in marks:
    total+=i
print(f"total is {total}")
percentage=((total/800)*100)
print(f"percentage is {percentage}")
if(percentage>=80):
    print("Excellent, You secured a distinction, really appreciated, keep going like this")
elif(percentage>=60 and percentage<80):
    print("Wow, You got a first class, congrats")
elif(percentage>=50 and percentage <50):
    print("Nice, second class, Try to Improve next time")
elif(percentage<50):
    print("It's okay, Don't be  disappointed, try something else, which is more apt for you or change your current styles/methods")
else:
    print("something wrong")

