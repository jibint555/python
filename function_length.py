#!/usr/bin/python3
word=input("Enter your desired string for finding the string: \t")
def length(data):
   length=0
   for _ in word:
      length+=1
   return length
for i in range(0, length(word)):
    print(f"Hello entry ----> {i} \n")




