#!/usr/bin/python3
age=int(input("Enter your age:\t"))

if age >= 18:
    taken_first_dose=input("Have you taken your first dose? (Y/N)")
    if taken_first_dose == 'y' or taken_first_dose == 'Y':
        print ("You're eligible for 2nd dose")
    else:
        print("Please visit your nearesr vaccine center at the earliest")


else:
    print("You're minor! Please continue to wear a mask and practice good hygiene") 
