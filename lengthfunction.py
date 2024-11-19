#!/usr/bin/python3
data=input("Enter string to find the count: \n")
def length():
    count=0
    for _ in data:
        count+=1
    
    print(f"total number of letter/digit in the given data {data} is {count} ")

length()
