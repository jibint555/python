#/usr/bin/python3
import random

r_num=random.randint(1, 1000)

n=int(input("Enter your number: \t"))
print(n)
print(f"System generated one is {r_num}")
if n == r_num:
   print("\n You're a lucky man")
else:
   print("\n You're unlucky, Try again, Good luck")

