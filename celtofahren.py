#!/usr/bin/python3
def celcious_to_fahrenheit(celcious):
    fahrenheit=(celcious *9/5)+32
    return fahrenheit

celcious=float(input("Enter the Celcious:\t"))
fahrenheit=celcious_to_fahrenheit(celcious)
print(f"{celcious}C is equal to {fahrenheit}F")


