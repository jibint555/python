#!/usr/bin/python
 
pass_marks=50
chemistry=70
physics=49
maths=62
biology=93
avg_marks=(chemistry+physics+maths+biology)/4
print(avg_marks)
if(chemistry>=pass_marks and physics>=pass_marks and maths>=pass_marks and biology>=pass_marks and avg_marks>pass_marks)==True:
    print("Passed")
else:
    print("Not Passed")
