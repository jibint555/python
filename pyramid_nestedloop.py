#!/usr/bin/python3
num=int(input("Enter the number of rows in your pyramid: \n"))
print("Here is the result: \n")
for i  in range(1, num):
    for j in range(0, i):
        print("*", end='\t')
        
    print("\n")
        
