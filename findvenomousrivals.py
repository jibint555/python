#!/usr/bin/python3
no_of_legs=int(input("Enter the number of legs:\t"))

if no_of_legs == 8:
   print("OMG, it's a Scorpion or spider")
   print("\U0001F577 \U0001F578")
elif no_of_legs > 100:
   print("Oh, It may be a Centipede")
else:
   print("mm, It may be a Worm!!!")

